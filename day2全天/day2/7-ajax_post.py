import urllib.request
import urllib.parse

ajax_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
cname = input("请输入要查询的城市：")
pageIndex = input("请输入人要查询的页码")
pageSize = input("请输入个数")

formdata = {
    'cname': cname,
    'pid': '',
    'pageIndex': pageIndex,
    'pageSize': pageSize,
}
#处理表单数据
formdata = urllib.parse.urlencode(formdata).encode('utf8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
#构建请求对象
request = urllib.request.Request(url=ajax_url,headers=headers)
response = urllib.request.urlopen(request,data=formdata)
print(response.read().decode('utf8'))