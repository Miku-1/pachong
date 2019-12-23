import requests

url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
proxy = {
    'http':'112.85.130.0:9999'
}
r = requests.get(url=url,headers=headers,proxies=proxy)
with open('daili.html','wb')as f:
    f.write(r.content)