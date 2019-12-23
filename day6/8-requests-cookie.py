import requests

#创建一个回话，往下所有get-post请求都要是用s来发送
#s.get()   s.post()
s = requests.session()
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019731422845'

formdata = {
    'email': '19992683234',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '1bb633acc5e3c276b697e328b6f60657c2ae67de09a37cb6109400fdbfca6b72',
    'rkey': '5f7a1d96ff48551fe2910f08a1a2ddcd',
    'f': 'http%3A%2F%2Fwww.renren.com%2F971784533%2Fnewsfeed%2Fphoto',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.renren.com',
    'Origin': 'http://www.renren.com',
    'Referer': 'http://www.renren.com/SysHome.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

r = s.post(url=post_url,data=formdata,headers=headers)
# print(r.text)

#到个人中心去
url = 'http://www.renren.com/971784533/profile'
ret = s.get(url=url,headers=headers)

with open('renren.html','wb')as f:
    f.write(ret.content)