# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time


def check_58_agent(mobile):
    url = 'https://hz.58.com/sou/?key={}'
    url = url.format(mobile.strip())

    headers = {
        'origin': 'https://hz.58.com',
        'referer': 'https://hz.58.com/sou/?key={}',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'cookie': 'f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; id58=pmbJqFyPWWQa2e6uU9seHg==; 58tj_uuid=5cbc21c9-7116-4da9-b9c0-5294f47f6e04; als=0; xxzl_deviceid=y%2F8zBymtHSkvNt8WcrBjOCv1syNoDyo6ZF4GLNODMaAionLnGQskSZK1P3cAcd%2BC; 58home=hz; city=hz; gr_user_id=5ca1bb01-f07c-4094-bd8f-cc08fbbcb372; wmda_uuid=5ac636c59b4505babd520ad7453de9e3; wmda_new_uuid=1; xxzl_smartid=e5b26e58f4cec89c764d5240d87bab1f; mcity=hz; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1553062483; wmda_visited_projects=%3B1409632296065%3B2385390625025%3B1731916484865%3B6333604277682; f=n; sessionid=5d0cdd65-25d9-4fa1-ad5c-e74002ede534; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1552991321,1553062424,1553139294; Hm_lvt_e15962162366a86a6229038443847be7=1552991321,1553062424,1553139294; _ga=GA1.2.54087471.1553139295; _gid=GA1.2.1398221871.1553139295; defraudName=defraud; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1553146692; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1553066689,1553154279; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1553154816; final_history=37170257275020%2C36962368527519%2C27494286302895; ppStore_fingerprint=3949478987B926686EAE4C79DB1DF677057EA82BE6FBA00B%EF%BC%BF1553162480404; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=hz%7C%E6%9D%AD%E5%B7%9E%7C0; new_uv=11; utm_source=market; init_refer=https%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fD4F9Y0K7k90nW_R0K3wuwT00000A-Pj7C00000LdvhU6.THYdr0K85yF9pywd0ZnqujnLPj-bmHfsnj0knjFbnfKd5Hu7fHDLnHnzPYPaPbR3PWb4f1Rdwjn3rjfzfbnLPbmd0ADqI1YhUyPGujY1nHbsnjbYPHTzFMKzUvwGujYkP6K-5y9YIZK1rBtEpMNVTAkdUhD8PH68mvqVQvbEnhfzXg9vrj6dnLmYnv4ouZD4usKWThnqrHDLP6%2526tpl%253Dtpl_11534_18997_15000%2526l%253D1510755689%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D58%252525E5%25252590%2525258C%252525E5%2525259F%2525258E-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%2525252C%252525E6%25252589%252525BE%252525E6%25252588%252525BF%252525E5%252525AD%25252590%2525252C%252525E4%252525B9%252525B0%252525E5%2525258D%25252596%252525E4%252525BA%2525258C%252525E6%25252589%2525258B%252525E8%252525BD%252525A6%2525252C%252525E5%2525259B%252525BD%252525E6%252525B0%25252591%252525E7%25252594%2525259F%252525E6%252525B4%252525BB%252525E6%2525259C%2525258D%252525E5%2525258A%252525A1%252525E5%252525B9%252525B3%252525E5%2525258F%252525B0%252525EF%252525BC%25252581%252526xp%25253Did%28%25252522m3190094572_canvas%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D108%2526ie%253DUTF-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D58%2526rqlang%253Dcn; new_session=0; wmda_session_id_1409632296065=1553221312155-d00151da-1c1c-71a2; Hm_lpvt_3bb04d7a4ca3846dcc66a99c3e861511=1553222279; Hm_lpvt_e15962162366a86a6229038443847be7=1553222280; GA_GTID=0d360415-0004-f68d-3096-b40ee57df0af; wmda_session_id_1731916484865=1553222512281-d5c05f35-a86d-36be; JSESSIONID=ED9F6299C50CD22BCD5196032BEAFB6B; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1553222721; hots=%5B%7B%22d%22%3A0%2C%22s1%22%3A%2213093735977%22%2C%22s2%22%3A%2213093734584%22%2C%22n%22%3A%22sou%22%7D%5D; xzfzqtoken=1ytfm1s09xqRdKd4NtaNizqoaXiSHbdslabNIEzbF2aTQ3iAPAp9oKnLgiAyZpzZin35brBb%2F%2FeSODvMgkQULA%3D%3D'
    }
    headers['referer'] = headers['referer'].format(mobile.strip())
    print(mobile, headers['referer'])
    resp = requests.get(url, headers=headers)
    return resp


def main():
    file_r = 'mobile_list_3_data.txt'
    file_a = 'mobile_list_58_true.txt'
    with open(file_r, 'r', encoding='utf-8') as r, \
            open(file_a, 'a', encoding='utf-8') as a:
        for line in r.readlines():
            line = line.replace('\n', '').split(',')

            if str(line[1]) == '1' and str(line[3]) == '浙江-杭州':
                res = check_58_agent(line[0])

                if '没有找到' in res.text:
                    soup = BeautifulSoup(res.text, 'lxml')
                    node = soup.find_all('p', class_='res')
                    print(node)
                    time.sleep(10)
                else:
                    time.sleep(10)
                    a.write('%s' % line[0].strip())
                    a.write('\n')


if __name__ == '__main__':
    main()

