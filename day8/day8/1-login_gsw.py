import requests
from bs4 import BeautifulSoup

#创建会话
s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

#向登陆页面发送请求，获取图片的链接,下载到本地
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r = s.get(url=url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
#找到图片的sc
image_src = 'https://so.gushiwen.org/' + soup.find('img',id='imgCode')['src']
#下载保存
img_ret = s.get(url=image_src,headers=headers)
with open('code.png','wb')as f:
    f.write(img_ret.content)

#获取表单中隐藏的值
viewstate = soup.find('input',id='__VIEWSTATE')['value']
viewg = soup.find('input',id = '__VIEWSTATEGENERATOR')['value']

code = input("请输入验证码")

#发送post请求
post_url = 'https://so.gushiwen.org/user/login.aspx?'

formdata = {
'__VIEWSTATE': viewstate,
'__VIEWSTATEGENERATOR': viewg,
'from': '',
'email': 'supernum_job@163.com',
'pwd': '123456',
'code': code,
'denglu': '登录',
}

#发送post请求
r = s.post(url=post_url,data=formdata)

with open('haha.html','wb')as f:
    f.write(r.content)


