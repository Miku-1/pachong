import requests

url = 'https://www.baidu.com/s?'
data = {
    'ie':'utf8',
    'wd':'美女',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
#发送请求data是一个原生字典
r = requests.get(url=url,params=data,headers=headers)
# print(r.json())

with open('baidu.html','w',encoding='utf8')as f:
    f.write(r.text)

with open('baidu2.html','wb')as f:
    f.write(r.content)



