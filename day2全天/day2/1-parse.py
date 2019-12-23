import urllib.parse

'''
urllib.parse.quote()
urllib.parse.unquote()
urllib.parse.urlencode()
'''
# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=吴亦凡&rsv_pq=bef1a6f100006382&rsv_t=1d70YI4TOrmopAwqFhNGmvK0Q23D1KB2LsYaGjJ%2BCDw7ohIFe5EwA8eXdqo&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=12&rsv_sug1=16&rsv_sug7=101'

# url = 'https://www.baidu.com/s?ie=utf-8&wd=吴亦凡'
# ret  = urllib.parse.quote(url)
# print(ret)
# '''
# https%3A//www.baidu.com/s%3Fie%3Dutf-8%26wd%3D%E5%90%B4%E4%BA%A6%E5%87%A1
# '''

# 'https://www.baidu.com/s?ie=utf-8&wd=%E5%90%B4%E4%BA%A6%E5%87%A1'

# url = 'https://www.goudan.com/index.html?name=%s&pwd=%s'%('狗蛋',123)

url = 'https://www.goudan.com/index.html?'
data = {
    'name':'狗蛋',
    'pwd':'123'
}
# it = []
# for k,v in data.items():
#     v = urllib.parse.quote(v)
#     it.append(k + '=' + v )
#
# info = '&'.join(it)
# url = url + info
# sss = urllib.parse.unquote(url)
# print(url)
# print(sss)

ret = urllib.parse.urlencode(data)
url+=ret
print(url)












