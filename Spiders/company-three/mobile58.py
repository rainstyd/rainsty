# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy
import requests
import requests
from collections import OrderedDict
import json
import time


# 数据去重
file_path = "./"


def whetherToRegister(mobile):
    # 58同城是否注册
    url_58 = 'https://passport.58.com/login/pc/dologin'
    payload = {
        'source': 'passport',
        'password': '1722fc4265e50b35dd5c4b1baf04760a390491f478fa9589e8fdc496813cd4a92ec18c6365394aba1a7645505ffd409424a70f43de0951e08417e790bee8097b9266c5457c79b613bfbd78902a1d2a48d809bc0d18f50270ed23025950daf1e33fea4235ac0f849ae8b49c5e2b681c8ab6499c12b22dc5fb249434040916f68f',
        'timesign': '',
        'isremember': 'false',
        'callback': 'successFun',
        'yzmstate': '',
        'fingerprint': 'C777F2640074D936A0F1D06DC53207F3D99A6D39CA3C94EA_011',
        'path': 'https://hz.58.com/?utm_source=market&pts=1552903040516',
        'finger2': 'en-US|24|2|4|1440_900|1440_900|-480|1|1|1|undefined|1|unknown|MacIntel|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|71c0f99212e160a9679f40fa874038a1',
        'username': '',
        'validcode': '',
        'vcodekey': '',
        'btnSubmit': '登录中...'
    }
    headers = {
        'origin': 'https://passport.58.com',
        'referer': 'https://passport.58.com/login?path=https://hz.58.com/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&ghid=0&PGTID=0d000000-0000-099d-2af0-6fe63c34865f&ClickID=1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'max-age=0',
        'content-length': '806',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'id58=pmbJqFyPWWQa2e6uU9seHg==; 58tj_uuid=5cbc21c9-7116-4da9-b9c0-5294f47f6e04; als=0; logintab_new=1; xxzl_deviceid=y%2F8zBymtHSkvNt8WcrBjOCv1syNoDyo6ZF4GLNODMaAionLnGQskSZK1P3cAcd%2BC; 58home=hz; city=hz; gr_user_id=5ca1bb01-f07c-4094-bd8f-cc08fbbcb372; wmda_uuid=5ac636c59b4505babd520ad7453de9e3; wmda_new_uuid=1; lastmobile=18317509215; xxzl_smartid=e5b26e58f4cec89c764d5240d87bab1f; loginstab_second=0; lastuname=18317509215; mcity=hz; hots=%5B%7B%22d%22%3A0%2C%22s1%22%3A%2213003634346%22%2C%22s2%22%3A%2213003632350%22%2C%22n%22%3A%22sou%22%7D%5D; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1552991321,1553062424; Hm_lvt_e15962162366a86a6229038443847be7=1552991321,1553062424; wmda_visited_projects=%3B1409632296065%3B2385390625025%3B1731916484865%3B6333604277682; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1553066689; final_history=27494286302895; GA_GTID=0d360415-0004-f424-c436-8effaea84f17; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; new_uv=6; utm_source=market; init_refer=https%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fD4F9Y0K7k90nW_R00-OFFT00000A-Pj7C00000nN7f50.THYdr0K85yF9pywd0ZnquWf4PHfvuj0snj0knyPhufKd5Hu7fHDLnHnzPYPaPbR3PWb4f1Rdwjn3rjfzfbnLPbmd0ADqI1YhUyPGujY1nHbsnjbYPHTzFMKzUvwGujYkP6K-5y9YIZK1rBtEpMNVTAkdUhD8PH68mvqVQvbEnhfzXg9vrj6dnLmYnv4ouZD4usKWThnqPjcYrHD%2526tpl%253Dtpl_11534_18997_15000%2526l%253D1510755689%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D58%252525E5%25252590%2525258C%252525E5%2525259F%2525258E-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%2525252C%252525E6%25252589%252525BE%252525E6%25252588%252525BF%252525E5%252525AD%25252590%2525252C%252525E4%252525B9%252525B0%252525E5%2525258D%25252596%252525E4%252525BA%2525258C%252525E6%25252589%2525258B%252525E8%252525BD%252525A6%2525252C%252525E5%2525259B%252525BD%252525E6%252525B0%25252591%252525E7%25252594%2525259F%252525E6%252525B4%252525BB%252525E6%2525259C%2525258D%252525E5%2525258A%252525A1%252525E5%252525B9%252525B3%252525E5%2525258F%252525B0%252525EF%252525BC%25252581%252526xp%25253Did%28%25252522m3190094572_canvas%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D108%2526ie%253DUTF-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D58%2526rqlang%253Dcn; new_session=0; pptmobile=18968004931; finger_session=0BWZV-x8t5bXyyO57e_iiOpPMl5hbjta; ppStore_fingerprint=3949478987B926686EAE4C79DB1DF677057EA82BE6FBA00B%EF%BC%BF1553137369469'
    }

    payload['username'] = mobile.strip()
    resp = requests.post(url_58, data=payload, headers=headers)
    print(resp.text)
    if 'success' in resp.text:
        if '不存在' in resp.text:
            return '58_false'
        elif '不符' in resp.text:
            return '58_true'
        elif '请输入图片验证码' in resp.text:
            return "请输入图片验证码"
    else:
        return '58_null'


def main():
    file_r = 'weizhuce58.txt'
    file_a = 'wb58_verify0001.txt'
    with open(file_r, 'r', encoding='utf-8') as r, open(file_a, 'a', encoding='utf-8') as a:
        for mobile in r.readlines():
            mobile = mobile.strip().split(',')
            for i in range(0, 10):
                try:
                    res = whetherToRegister(mobile[0])
                    if res is None and i < 9:
                        continue
                    elif res == '请输入图片验证码':
                        time.sleep(10)
                        break
                    elif i == 9:
                        res = 'none'
                        mobile.append(res)
                        a.write(','.join(mobile))
                        a.write('\n')
                        print('end...')
                    else:
                        mobile.append(res)
                        a.write(','.join(mobile))
                        a.write('\n')
                        print('end...')
                        break
                except BaseException as e:
                    print(e)
                    time.sleep(10)
                    continue


if __name__ == '__main__':
    main()
