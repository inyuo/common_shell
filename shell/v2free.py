# -*- coding: utf8 -*-
# python >=3.8

import requests, time

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 登录
def login(user, password):
    url1 = "https://w1.v2free.net/auth/login"
    headers = {}
    data1 = {
        "email": user,
        "passwd": password,
        "code": "",
        "remember_me": ""
    }
    r1 = requests.post(url1, data=data1, headers=headers, allow_redirects=False)
    if r1.status_code > 400:
        return 0
    cookie_items = r1.cookies.get_dict()
    print("access_code获取成功！")
    return cookie_items


# 主函数
def main(user, password):
    user = str(user)
    password = str(password)
    if user == '' or password == '':
        print("用户名或密码填写有误！")
        return
    # 1.登录获取cookie
    login_token = login(user, password)
    if login_token == 0:
        print("登陆失败！")
        return "login fail!"
    cookies = ''
    for key, values in login_token.items():
        cookies = cookies + key + '=' + values + ';'

    # 2.签到
    url = 'https://w1.v2free.net/user/checkin'
    head = {
        "Cookie": cookies,
    }
    data2 = {}
    response = requests.post(url, data=data2, headers=head).json()

    # print(response)
    result = now
    result += "：" + user
    if response['ret'] == 0:
        result += '今日已签到'
    else:
        result +='#签到成功-' + str(response['trafficInfo'])
    print(result)
    return result


if __name__ == "__main__":
    # 多账号 ”#分割“
    email = "q669239799@163.com"
    passwd = "wujinyu1111"

    main(email, passwd)

    print("任务结束:"+now)