import json
lt = [
    {'name':'郝岩','age':16,'height':'160'},
    {'name':'米刚','age':2,'height':'30'},
    {'name':'赵莹','age':16,'height':'80'},
    {'name':'宝钢','age':3,'height':'15'}
    ]

string = json.dumps(lt,ensure_ascii=False)
# print(type(string))
print(string)
# obj = json.loads(string)
# print(obj)