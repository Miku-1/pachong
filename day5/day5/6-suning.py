import urllib.request
import json,jsonpath

url = 'https://review.suning.com/ajax/cluster_review_lists/general-30075272-000000000627657477-0000000000-total-2-default-10-----reviewList.htm?callback=reviewList'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)
content = urllib.request.urlopen(request).read().decode('utf8')
content = content.strip('reviewList()')
obj = json.loads(content)
#找到所有的品论列表
comments = obj['commodityReviews']
fp = open('苏宁评论.txt','w',encoding='utf8')
for comment in comments:
    #评论时间
    publishTime = comment['publishTime']
    #用户
    nickname = comment['userInfo']['nickName']
    #评论内容
    content = comment['content']
    #图片地址
    is_have = comment['picVideoFlag']
    if is_have == True:
        image_src = jsonpath.jsonpath(comment,'$..imageInfo[*].url')
    else:
        image_src = "无"

    #保存
    item = {
        '评论时间':publishTime,
        '用户':nickname,
        '评论内容':content,
        '图片地址':image_src,
    }
    string = str(item)
    fp.write(string + '\n')












