import urllib.request
import urllib.parse
import http.cookiejar

#在代码中保存cookie
#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
#通过cj创建一个headler
handler = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(handler)
#提交地址
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019731422845'
# post_url1 = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20197314973'

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

#处理表单数据
formdata = urllib.parse.urlencode(formdata).encode('utf8')

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

request =urllib.request.Request(url=post_url,headers=headers)

response = opener.open(request,data=formdata)
# print(response.read().decode('utf8'))

#访问登陆后的资料详情页面
pro_url = 'http://www.renren.com/971784533/profile'
request1 = urllib.request.Request(url=pro_url,headers=headers)
response1 = opener.open(request1)

with open('moni1.html','wb')as f:
    f.write(response1.read())







