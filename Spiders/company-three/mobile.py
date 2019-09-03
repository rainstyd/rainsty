# -*- coding: utf-8 -*-
import os
import requests
import time


def verifyPhoneNumberStatus():
    # 验证手机号状态
    file_path = "./"
    apikey = 'ddfd6009bf254f779f3ee303fb8094de'
    url = 'http://apis.haoservice.com/thirdnode/phonenotest/'
    no_status_dict = {
        '0': '空号', '1': '实号', '2': '停机', '3': '库无', '4': '沉默号', '5': '风险号'
    }

    def get_mobile_no(mobile):
        print(mobile)
        mobile = mobile.strip()
        resp = requests.get(url, params={'key': apikey, 'mobiles': mobile},
                            headers={'Content-Type': 'application/json'})
        print(resp.status_code)
        # 需要修改，200的时候，{"error_code":10007,"reason":"未知的请求源，（服务器没有获取到IP地址）","result":null}
        print(resp.text)
        try:
            if str(resp.status_code) == '200':
                resp_json = resp.json()
                res = resp_json.get('result')
                status = res.get('status')
                area = res.get('area')
                if res.get('area') is None:
                    area = 'none'
                numberType = res.get('numberType')
                if res.get('numberType') is None:
                    numberType = 'none'
                return [mobile, res.get('status'), no_status_dict.get(str(status)), area, numberType]
            else:
                return False
        except BaseException as e:
            print(e)
            return False

    no_mobile_filename = os.path.join(file_path, 'mobile_list_3.txt')
    right_mobile_filename = os.path.join(file_path, 'mobile_list_3_data.txt')

    with open(right_mobile_filename, 'a', encoding='utf-8') as f, open(no_mobile_filename, 'r') as f_mobiles:
        for mobile in f_mobiles.readlines():
            if mobile != '\n':
                res = get_mobile_no(mobile)
                print(res)
                if res is not False:
                    f.write(','.join(res))
                    f.write('\n')
            # time.sleep(1)


def main():
    verifyPhoneNumberStatus()


if __name__ == '__main__':
    main()
