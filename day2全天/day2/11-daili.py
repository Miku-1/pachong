import urllib.request

#创建handler
handler = urllib.request.ProxyHandler(proxies={'http':'58.216.156.38:80'})
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com/s?ie=utf8&wd=ip'

response = opener.open(url)
with open('dali.html','wb')as f:
    f.write(response.read())