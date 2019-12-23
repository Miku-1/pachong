import urllib.request
url = 'http://www.baidu.com/'
#创建一个handler对象
handler = urllib.request.HTTPHandler()
#通过handler创建一个opener
opener = urllib.request.build_opener(handler)
#这个opener有个方法open方法，就类似于urlopen()
response = opener.open(url)
print(response.read().decode('utf8'))