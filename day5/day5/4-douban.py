import urllib.request
from lxml import etree
import json

#url
url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=10'
#headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
content = urllib.request.urlopen(request).read().decode('utf8')
#content格式为json
lt = []
#将其转化为python对象
obj = json.loads(content)
# print(obj)
for movie in obj:
    #要海报
    image_src = movie['cover_url']
    #要名称
    title = movie['title']
    #要评分
    score = movie['score']
    #评价人数
    vote_count = movie['vote_count']
    #国家
    regions = movie['regions']
    # print(regions)
    # print(type(regions))
    item = {
        '电影海报':image_src,
        '电影名称':title,
        '电影评分':score,
        '评分人数':vote_count,
        '地区国家':regions
    }
    lt.append(item)
#保存
string = json.dumps(lt,ensure_ascii=False)
with open('movie.txt','w',encoding='utf8')as f:
    f.write(string)

