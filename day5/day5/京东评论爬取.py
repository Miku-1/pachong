# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/16 17:47
    @File   : 京东评论爬取.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import urllib.parse
import urllib.request
import json,jsonpath

def gethtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    request = urllib.request.Request(url=url,headers=headers)
    content = urllib.request.urlopen(request).read().decode('utf8')
    return content
query_string = {
    'callback': 'fetchJSON_comment98vv882',
    'productId:':' 30718880816',
    'score': '0',
    'sortType':'5',
    'page': '5',
    'pageSize': '10',
    'isShadowSku':'0',
    'rid': '0',
    'fold': '1'
}
url ='https://sclub.jd.com/comment/productPageComments.action?'
url = url + urllib.parse.urlencode(query_string)
content = gethtml(url)
print(content)
obj = json.loads(content)

# fp = open('京东评论.txt','w',encoding='utf8')
for i in obj['questionList']:
    print(i['content'])
