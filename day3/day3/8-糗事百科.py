import urllib.request
import urllib.parse
import re,os,time
'''
拼接url,发送请求，得到响应内容，分析响应内容，保存数据
'''
def get_request(new_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    request = urllib.request.Request(url=new_url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf8')

def parse_content(content):
    '''
    <div class="thumb">
        <a href="/article/122125840" target="_blank">
            <img src="//pic.qiushibaike.com/system/pictures/12212/122125840/medium/EAB3PVYM1XFGJF1A.jpg" alt="是胖到下巴都是肉的我">
        </a>
    </div>
    '''
    patten = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)" />.*?</div>',re.S)
    ret = patten.findall(content)
    # print(ret)
    # print(len(ret))
    down_load(ret)
#
def down_load(ret):
    dirname = 'qiutu'
    for tp in ret:
        #取出图片地址
        image_url = 'https:' + tp[0]
        #取出图片名称
        image_name = tp[1]
        #生成文件夹名字
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = image_name + '.'+ image_url.split('.')[-1]
        filepath = os.path.join(dirname,filename)
        print('正在下载图片%s。。。。'%filename)
        urllib.request.urlretrieve(image_url,filepath)
        print('结束下载图片%s。。。。'%filename)
        time.sleep(2)

def main():
    #输入起始页码
    start_page = int(input("请输入起始页码"))
    end_page =int(input("请输入结束页码"))
    url = 'https://www.qiushibaike.com/pic/page/'
    for page in range(start_page,end_page+1):
        print("正在下载第%s页....."%page)
        #拼接url
        new_url = url + str(page) + '/'
        request = get_request(new_url)
        content = get_content(request)
        parse_content(content)
        print("结束下载第%s页....." % page)
        time.sleep(2)


if __name__ == '__main__':
    main()