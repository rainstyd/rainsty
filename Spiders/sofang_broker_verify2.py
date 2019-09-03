# -*- coding: utf-8 -*-
import json
import requests
import time


def whetherToRegister(mobile):
    url = 'http://agent.sofang.com/auth/login'
    payload = {
        'userName': '',
        'password': '854f56472e8b035e79df587a3e17d2b7',
        '_token': 'ko0u2jFzfkqWqp32zFbqNnIB7fe8UwpQfNZiMCLO'
    }
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'connection': 'keep-alive',
        'content-length': '110',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'uniqueName=29be1c35072b7f89aa4c37a3df883558; UM_distinctid=169a47e406214c-0b543beab08f4e-3d644509-100200-169a47e4063301; www_sofang_session=eyJpdiI6IlpWRlZGd2Y5eUVsZ1Q2Y0g2UE9GTUE9PSIsInZhbHVlIjoiMWdUekVPUWpBY003d2htaGtUdzAyaEI1K3hndEhuXC91d3didHhIb3hVSjlFQ1JmTVg1R1ZzUVllV2I5Y2xRUWpnWXFLUW9iNkpibVFVMTMrOHVYejVBPT0iLCJtYWMiOiJjOWJkZTk1NzA1YjFkYzJkZmM2NDAyMjA4YTliYjgyYmFjMzhmNTA3ZmYyNmMzMzUxZGUzMTAyOTg4MzRiNDFiIn0%3D; cityid=eyJpdiI6InoxaXRkdjVidkR4MzlDSkhkQm5sWXc9PSIsInZhbHVlIjoiWjJrMTRVSWdtUkk2YWJYYUNwNVloZz09IiwibWFjIjoiMDI1OGY5Zjc4ODA1MmE5MDZiNmE1YTgwYjBlYjE1YWM5MGJlNGJiNTEyYTcwY2JlOGYzZThlYjZlMWNlNzEyZCJ9; city=eyJpdiI6IjVYOXczeWdqbWxINzZDTW1KZHdHM3c9PSIsInZhbHVlIjoibmI5anZUeW1vUDNsd0V4cjFGeHRyTTV4VFdDenU0cGZHYUZzVEV1UE5CRXhxMWlUVmtpYk1mUzQ4dFFcL2paUVBvTzNBVlZDSnZUXC9FNEdLZURqS25vZEZBTWRpOE5zZ3NsaSt5c2hoZWRMbG5ERzJlVFJ0aTRJMWVrSjdNS2FmMG1RdlFzT3hYeXRWV2dnMDNLUTdlNyszdThPbnJYVjk2aFd4RmtSR2IweWR0VmkyOThrMjdXQmpxc3BLOWkyMnc0NG55THhLd1ZoM1l5TjhxT252K1laOCsrVTMwSnAwQ2RuWGRzeWFiNDdHTE9WbGc4QmxrSE52STQ1cG44WGdpckl5YURROHREUCtMQjZNcUxoT2k1QktyQTMyRWNyVlFEM0pqdlNpWGRDZz0iLCJtYWMiOiIwMDVmZmE1NGI3ZWU1MjRkZTU3YzcwMzAyMTMyMjJlOGQxZDYxOTE3MGFiMjdkOWE3N2EyMTBjNjQ0NTBlYjY0In0%3D; citypy=eyJpdiI6ImU1U1BtSXJOWGpBdWJhdDRUVGZlOEE9PSIsInZhbHVlIjoiYmlTTFlYakZZa2FvcHhudFNNSlBYdz09IiwibWFjIjoiZTY1MDY2YzhlNGIwNDdkZGViNmE1YzI1NmM2YzFhYTM3OGViMDE5YTFhNDRmNmJiNjMyMDBhYTg0OTE1NzI2NyJ9; agent_sofang_session=0e46d72e4d04779d4d3100285a2213835f2b3b2d; XSRF-TOKEN=eyJpdiI6IllGTDh2MnExd252NENZU2QyYjNXN1E9PSIsInZhbHVlIjoiRWM3TVk5enppQXc5T2JqTlNOQ3ZjeXQ2eHJcL1lJNmcyc3czTTBSSGN2ZTd4YjZpa3BXZ3hXMHRYSUREbjFaY2M3TW9HUTMxUTZiQVwvcU9JZWs5VHFtUT09IiwibWFjIjoiNWU1MDNiNThmODE3ZjNlMGI5MzNiYzJhOTE1ZGU1Y2M0Mzc0MDBhMGQxMTdkMTY3NzcxYTQ1NjZlMmY4MWU2ZSJ9',
        'origin': 'http://agent.sofang.com',
        'referer': 'http://agent.sofang.com/majorLogin?type=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    payload['userName'] = mobile.strip()
    return requests.post(url=url, data=payload, headers=headers)


def main():
    file_r = 'mobile_list_50000.txt'
    file_a = 'sf_broker2_list001.txt'
    with open(file_r, 'r', encoding='utf-8') as r, open(file_a, 'a', encoding='utf-8') as a:
        for line in r.readlines():
            line = line.replace('\n', '').split(',')
            print(line[0])
            res = whetherToRegister(line[0]).text

            if str(res) == '2':
                line.append('否')
            elif str(res) == '0':
                line.append('是')
            else:
                line.append('none')

            a.write(','.join(line))
            a.write('\n')


if __name__ == '__main__':
    main()
