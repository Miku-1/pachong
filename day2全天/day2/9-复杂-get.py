import urllib.request
import urllib.parse
import os,time

# 'kw=python&ie=utf-8&pn=0'
#输入贴吧名字-起始页码-终止页码
bname = input("请输入贴吧名字")
start_page = int(input("请输入起始页码"))
end_page = int(input("请输入终止页码"))
#不完整的url
url = 'http://tieba.baidu.com/f?'
#通过循环，循环获取拼接每一页的url,得到每一页的内容
for page in range(start_page,end_page+1):
    pn = (page-1)*50
    #定义参数字典
    data = {
        'kw':bname,
        'ie':'utf8',
        'pn':pn
    }
    #将data转化为query_string
    query_string = urllib.parse.urlencode(data)
    #拼接得到url
    new_url = url + query_string
    # print(new_url)

    #构建请求对象
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    request = urllib.request.Request(url=new_url,headers=headers)
    #创建一个bname的文件夹
    if not os.path.exists(bname):
        os.mkdir(bname)
    #发送请求得到响应
    response = urllib.request.urlopen(request)
    #生成文件名字
    filename = '%s-第%s页.html'%(bname,page)
    #拼接文件路径
    filepath = os.path.join(bname,filename)
    print("正在下载%s------"%filename)
    #将内容写入到filepath中
    with open(filepath,'wb')as f:
        f.write(response.read())
    print("结束下载%s------" % filename)
    time.sleep(3)



















