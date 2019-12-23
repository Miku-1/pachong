import re
string = '<div>貂蝉</div><div>小乔</div><div>妲己</div><div>武则天</div><div>虞姬</div>'
patten = re.compile(r'<div>(.*?)</div>')
ret = patten.findall(string)
print(ret)

#忽略大小写
string = 'l lOve Python veRy mUch'
patten = re.compile(r'LOVE',re.I)
ret = patten.search(string)
print(ret.group())

#多行模式
# string = '我爱你，爱着你,' \
#          '我们不一样，' \
#          '我和你吻别，' \
#          '我爱你中国，' \
#          '爱上一个不回家的男人'
#
# patten = re.compile(r'^我爱你>',re.M)
# ret = patten.findall(string)
# print(ret)

#单行模式
string = '''<div>细思极恐
你的对手在看书，
你的敌人在磨刀。
你的闺蜜在减肥，
隔壁老王在练腰.</div>
'''
# print(string)

patten = re.compile(r'<div>(.*?)</div>',re.S)
ret = patten.search(string)
print(ret.group(1))








