import jsonpath
import json

fp = open('book.json','r',encoding='utf8')
string = fp.read()
# print(string)
fp.close()
# print(string)
obj = json.loads(string)
#使用jsonpath
# ret = jsonpath.jsonpath(obj,'$.store.book[*].author')
# ret = jsonpath.jsonpath(obj,'$..author')
# ret = jsonpath.jsonpath(obj,'$.store.*')
# ret = jsonpath.jsonpath(obj,'$.store..price')
#索引下标，无倒序
# ret = jsonpath.jsonpath(obj,'$..book[1]')
# print(ret)
# ret = jsonpath.jsonpath(obj,'$..book[2:3]')
# print(ret)
