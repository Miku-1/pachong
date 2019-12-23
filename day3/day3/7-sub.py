import re

string = '男人都喜欢20岁的女孩'
patten = re.compile(r'\d+')
# ret = patten.sub('21',string)
# print(ret)

#该函数必须有一个参数，是个对象
#该函数必须有一个返回值，字符串，用返回值替换匹配的内容
def fn(obj):
    num = int(obj.group())+1
    return str(num)
ret = patten.sub(fn,string)
print(ret)

#看闭包函数











