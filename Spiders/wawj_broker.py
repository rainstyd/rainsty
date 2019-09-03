# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time


def whetherToRegister(page):
    url = 'https://hz.5i5j.com/jingjiren/n{}/'
    url = url.format(page.strip())
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'yfx_c_g_u_id_10000001=_ck19032217452316231370785317386; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A170%3A%3Apmf_from_adv%3A%3Ahz.5i5j.com%2F; ershoufang_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_13149933751%253Fzn%253D13149933751%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%252213149933751%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_18968004932%253Fzn%253D18968004932%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%252218968004932%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; yfx_s_u_id_10000001=6279938; yfx_s_u_name_10000001=18968004932; user_info=TBYRRFZKXlNdAUFbEANZDgUJVQMECQYKQ08VXF1RDgtRXVUSChJCUVleQ0RJEhwSRUNVQnlUEgoSBgIHCQkDCBJN; wiwj_token_ticket=ST-106777-gE1quIitfFJKyfFSHheb-passport.5i5j.com; wiwj_token_ST-106777-gE1quIitfFJKyfFSHheb-passport.5i5j.com=%7B%22uid%22%3A%226279938%22%7D; jingjiren_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fjingjiren%252F_18968004932%253Fzn%253D18968004932%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%252218968004932%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fjingjiren%252F_13149933751%253Fzn%253D13149933751%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%252213149933751%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; _ga=GA1.2.62529311.1553264279; domain=hz; baidu_OCPC_pc=9b0365a45d1dd407fcb10009db737436e9719374b2a29e9da9edf86537231394a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22baidu_OCPC_pc%22%3Bi%3A1%3Bs%3A178%3A%22%22https%3A%5C%2F%5C%2Fhz.5i5j.com%5C%2F%3Fpmf_group%3Dbaidu%26pmf_medium%3Dppzq%26pmf_plan%3D%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%26pmf_unit%3D%25E6%25A0%2587%25E9%25A2%2598%26pmf_keyword%3D%25E6%25A0%2587%25E9%25A2%2598%26pmf_account%3D170%22%22%3B%7D; yfx_f_l_v_t_10000001=f_t_1553247923509__r_t_1553475097927__v_t_1553475097927__r_c_1; _Jo0OQK=48DA196421C54858FFA42111EF840F6106FC6625CF95A516EDABADEA3D0EC9EBDE0943988662D0FF8CFB6CFE1F4019E064C734261D272470A098F4DCCF92DA21B74FFBBE0C390CBD8D41F7A141E52F240311F7A141E52F2403120C3BC8E94B972B0800EF17EA71E8444GJ1Z1OQ==; PHPSESSID=lmivhhs9uovt0p6n6uro57c6lr; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A5i5j%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A170%3A%3Apmf_from_adv%3A%3Ahz.5i5j.com%2F; yfx_key_10000001=5i5j; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1553247924,1553264280,1553475098,1553475232; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1553475251',
        'Host': 'hz.5i5j.com',
        'Referer': 'https://hz.5i5j.com/jingjiren/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    print(url)
    return requests.get(url, headers=headers).text


def main():
    list = []
    file_a = 'wawa_broker_info.txt'

    for r in range(1, 200):
        try:
            for n in range(0, 100):
                res = whetherToRegister(str(r))
                if '联系方式' in res:
                    soup = BeautifulSoup(res, 'lxml')
                    node_name = soup.find_all('span', class_='name')
                    node_mobile = soup.find_all('div', class_='contacty')

                    for a in range(0, 100):
                        try:
                            name = re.findall(r'<h3>(.*)</h3>', str(node_name[a]))
                            mobile = re.findall(r'<span>(.*)</span>', str(node_mobile[a]))
                            print(name[0], mobile[0])
                            list.append('%s, %s\\n' % (str(name[0]), str(mobile[0])))
                        except IndexError:
                            break
                    break
                else:
                    time.sleep(10)
                    continue

        except IndexError:
            break
        time.sleep(10)

    with open(file_a, 'a', encoding='utf-8') as a:
        a.write(','.join(list))


if __name__ == '__main__':
    main()

