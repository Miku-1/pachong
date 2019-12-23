import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}


# response = urllib.request.urlopen(url)
# # print(response.getcode())

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.getcode())