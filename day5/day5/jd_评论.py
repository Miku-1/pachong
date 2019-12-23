# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/16 18:21
    @File   : 22.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
#

#
# url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv12994&productId=100004323294&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
# headers={'Referer':'https://item.jd.com/100004323294.html',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
#
#         }
# # 获取网页信息
# req=requests.get(url ,timeout=30,headers=headers)
# # print(req.text)
#
# #先把不用的内容去掉，再用json库解析它，得到我们想要的东西
# jd=json.loads(req.text.lstrip("fetchJSON_comment98vv12994(").rstrip(");"))
#
# #遍历出每条评价
# fp = open('京东评论.txt','w',encoding='utf8')
# for i in jd['comments']:
#     string = ">>>"+"\n"+i['content'].strip() + '\n'
#     print(string)
#     fp.write(string)
# fp.close()
# tmp = set()
# def test():
#     seen = set()
#     while 1:
#          a = yield
#          yield a
#          seen.add(a)
# a = test()
#
# a.close()

def merge(left,right):
    c = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            c.append(left[a])
            a += 1
        else:
            c.append(right[b])
            b += 1
    if a == len(left):
        for i in right[b:]:
            c.append(i)
    else:
        for i in left[a:]:
            c.append(i)
    return c
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left,right)


nums = [1,2,34,9,72,8,12,34]
print(merge_sort(nums))






