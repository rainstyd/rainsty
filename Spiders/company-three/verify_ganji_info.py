# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time


def check_ganji_agent(mobile):
    url = 'http://hz.ganji.com/site/s/_{}/'
    url = url.format(mobile.strip())

    headers = {
        'origin': 'http://hz.ganji.com/',
        'referer': 'http://hz.ganji.com/site/s/_{}/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'cookie': "statistics_clientid=me; ganji_xuuid=a88e96eb-18cf-4fbe-8fad-cc983465961d.1553049314327; ganji_uuid=9414419739401157990460; lg=1; xxzl_deviceid=qAE2S%2BTMlFh6ng3Cl9Ea8rTZ0cOe%2FwLUZuwI4GSUh1qF%2B1cHsF4mvfxaE60uBP72; xxzl_smartid=e5b26e58f4cec89c764d5240d87bab1f; citydomain=hz; vip_version=new; SiftRecord['1553063114']=13003665133%3C%E6%B1%82%E8%81%8C%E7%AE%80%E5%8E%86%3E%7C%7C%2Fqiuzhi%2Fs%2F_13003665133%2F; bdshare_firstime=1553066019840; gj_footprint=%5B%5B%22%5Cu8425%5Cu4e1a%5Cu5458%5C%2F%5Cu5e97%5Cu5458%22%2C%22%5C%2Fzpyingyeyuan%5C%2F%22%5D%5D; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1553066307; GANJISESSID=2ecrpe0tbhcfps651uo439j7uu; SiftRecord['1553221483']=13071828243%3C%E8%B5%B6%E9%9B%86%E6%9C%8D%E5%8A%A1%3E%7C%7C%2Fhuangye%2Fs%2F_13071828243%2F; Hm_lvt_4217cebb17f3dd0ee322100b5054dda0=1553066019,1553221589; Hm_lpvt_4217cebb17f3dd0ee322100b5054dda0=1553221589; Hm_lvt_2309589db5417bfe7a4ec0d5d5daa6b5=1553066019,1553221589; Hm_lpvt_2309589db5417bfe7a4ec0d5d5daa6b5=1553221589; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A37014896621%2C%22kw%22%3A%2213093781535%22%7D; ganji_login_act=1553226118313"
    }
    headers['referer'] = headers['referer'].format(mobile.strip())
    print(mobile, headers['referer'])
    resp = requests.get(url, headers=headers)
    return resp


def main():
    file_r = 'ganji_true.txt'
    file_a = 'mobile_list_ganji_true.txt'
    with open(file_r, 'r', encoding='utf-8') as r, \
            open(file_a, 'a', encoding='utf-8') as a:
        for line in r.readlines():
            line = line.replace('\n', '').split(',')

            if str(line[1]) == '1' and str(line[3]) == '浙江-杭州':
                res = check_ganji_agent(line[0])

                if '抱歉' in res.text:
                    soup = BeautifulSoup(res.text, 'lxml')
                    node = soup.find_all('span', class_='f_c_red')
                    print(node)
                    time.sleep(1)
                else:
                    a.write('%s' % line[0].strip())
                    a.write('\n')


if __name__ == '__main__':
    main()

