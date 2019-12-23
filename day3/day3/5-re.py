import re

#如何使用
#match search findall compile sub
'''
match :从字符串开头匹配，失败返回none
seach: 从任意位置开始匹配，匹配失败返回none，只能匹配一个，返回一个对象，ret.group()查看匹配结果
'''

#生成正则对象
string = '<div><span>一骑红尘妃子笑，无人知是荔枝来</span></div>'
# patten = re.compile(r'<\w+><\w+>.*</\w+></\w+>')
patten = re.compile(r'<(\w+)><(\w+)>(.*)</\2></\1>')
ret =patten.match(string)

print(ret.group())
print(ret.group(1))
print(ret.group(3))