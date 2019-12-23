import urllib.request

# url = 'http://www.baidu.com'
#
# response = urllib.request.urlopen(url)
#得到的是一个响应对象
# print(response.read())
#打印出来是二进制内容
#状态码
# print(response.getcode())
#获取url
# print(response.geturl())
#获取
# print(response.getheaders())
# print(response.read().decode('utf8'))
#把读取的响应内容保存起来
# with open('baidu.html','w',encoding='utf8')as f:
#     f.write(response.read().decode('utf8'))

# with open('baidu2.html','wb')as f:
#     f.write(response.read())
#str  --->   bytes
#  encode（）
#bytes  ---->  sty
#  decode()


#下载美女图片

# url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565609432670&di=ca217825b98a2f024bf76278d0c83b57&imgtype=0&src=http%3A%2F%2Fimg2.ph.126.net%2F2zB3_wWPXlEW0RdwQa8d6A%3D%3D%2F2268688312388037455.jpg'

#发送请求，得到相应对象
# response = urllib.request.urlopen(url)
#写入到文件
# with open('img.jpg','wb')as f:
#     f.write(response.read())

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565610240539&di=c38ad931db13735c21d9f64379219b23&imgtype=0&src=http%3A%2F%2Fws2.sinaimg.cn%2Flarge%2F9150e4e5ly1fctr9wtkeej20j60j6gmk.jpg'

urllib.request.urlretrieve(url=url,filename='np.jpg')



