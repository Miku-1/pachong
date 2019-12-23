import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
fromdata = {
    'from': 'en',
    'to': 'zh',
    'query': 'baby',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '814534.560887',
    'token': 'b0ad4a207ae40f7b0a84cb4fe68785c7',
}

#构建请求对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
request = urllib.request.Request(url=post_url,headers=headers)
#首先对post参数进行处理
fromdata = urllib.parse.urlencode(fromdata).encode('utf8')
# print(type(fromdata))
response = urllib.request.urlopen(request,data=fromdata)
print(response.read().decode('utf8'))




