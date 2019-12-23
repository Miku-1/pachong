import urllib.request
import urllib.parse

#输入关键字
kw = input('请输入关键字')
url = 'https://www.baidu.com/s?'
#get参数
data = {
    'ie':'utf8',
    'wd':kw,
}
#首先将字典转化为query_string格式
query_string = urllib.parse.urlencode(data)
#拼接url
url += query_string

#构建一个请求对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
#打开文件保存信息
filename = kw + '.html'
with open(filename,'wb')as f:
    f.write(response.read())











