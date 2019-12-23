import urllib.request
import base64

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&oq=%25E9%2598%25BF%25E5%25B8%2583%25E4%25BA%2591&rsv_pq=bd5d74a5004fc6b0&rsv_t=228a0wm08WiExWIaoDVNZ2u4RlEWVHpVo8t4n6%2F%2BYVXmFCTBv06iSZzW9%2Fc&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=4&rsv_sug7=101&bs=%E9%98%BF%E5%B8%83%E4%BA%91'

user = 'HB06U73Y03952H0D'
pwd = '72CA4141CE3CE118'
string = user + ':' + pwd
#将指定的字符串进行base64编码
encodestr = 'Basic ' + base64.b64encode(string.encode('utf-8')).decode('utf-8')
# print(encodestr)

headers = {
    'Proxy-Authorization':encodestr
}

#构建请求对象
request = urllib.request.Request(url=url,headers=headers)
#构建handler,opener
proxy = {'http':'http-dyn.abuyun.com:9020'}
handler = urllib.request.ProxyHandler(proxies=proxy)
opener = urllib.request.build_opener(handler)

response = opener.open(request)
print(response.read().decode('utf8'))

with open('ipdaili.html','wb')as f:
    f.write(response.read())