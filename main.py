
def print_hi(name):
    print("Hi, "+name)


if __name__ == "__main__":
    print_hi('PyCharm')

    cookieItems = {'email': 'q669239799%40163.com', 'expire_in': '1647786534', 'ip': '942b00aa6a9a640c4522022f8b14f96b', 'key': '782f372c92860dfb8d8bdddf8580e1917d5b0205dcab0', 'uid': '10731'}

    cookies = ''
    for key, values in cookieItems.items():
        cookies = cookies+key+':'+values+';'
    print(cookies)


