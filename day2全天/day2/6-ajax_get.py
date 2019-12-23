import urllib.request
import urllib.parse

ajax_url= 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&'

page = int(input("请输入要获取的页数"))
page2 = page*20
# 1      0  20
# # 2      0  40
# # 3      0  60
query_string = {
    'start': '0',
    'limit': page2,
}
#拼接url
query_string = urllib.parse.urlencode(query_string)
ajax_url += query_string
#构建请求对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

request = urllib.request.Request(url=ajax_url,headers=headers)
response = urllib.request.urlopen(request)
with open('douban.txt','wb')as f:
    f.write(response.read())
