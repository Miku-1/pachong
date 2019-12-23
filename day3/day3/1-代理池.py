import urllib.request
import random,time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
#随机从文件中读取一个代理
fp = open('daili.txt','r')
content = fp.read()
#将内容以换行符\n分割
lt = content.split('\n')
print(lt)

while True:
    #随机抽取一个代理，拼接格式
    daili = random.choice(lt)
    proxy = {'http':daili}
    handler = urllib.request.ProxyHandler(proxies=proxy)
    opener = urllib.request.build_opener(handler)
    url = 'https://www.baidu.com/s?ie=utf8&wd=ip'

    request = urllib.request.Request(url=url, headers=headers)
    try:
        response = opener.open(request)
        print('代理使用成功%s'%daili)
        with open('dail.html','wb')as f:
            f.write(response.read())
    except Exception as e:
        print("代理使用失败%s"%daili)
        lt.remove(daili)
        print(e)
        time.sleep(2)

