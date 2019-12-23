from bs4 import BeautifulSoup
import urllib.request
import time

def get_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    return content

def parse_content(content):
    #生成soup对象
    soup = BeautifulSoup(content,'lxml')
    #根据方法查找所有的章节和内容
    odiv = soup.find('div',class_="book-mulu")
    # print(odiv)
    get_text(odiv)

def get_string(href):
    #构建请求对象
    request = get_request(href)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    #生成soup对象
    soup = BeautifulSoup(content,'lxml')
    #找到章节内容
    odiv = soup.find('div',class_="chapter_content")
    #返回内容
    return odiv.text


def get_text(odiv):
    #生成soup对象
    # soup = BeautifulSoup(odiv,'lxml')
    #根据方法查找所有的章节a链接
    oa_list = odiv.find_all('a')
    # print(len(oa_list))
    #便利列表，得到每一个a对象的链接和标题
    fp = open('三国演义.txt','w',encoding="utf8")
    for oa in oa_list:
        #得到标题
        title = oa.string
        print("正在下载----%s"%title)
        # print(title)
        #得到链接
        href = 'http://www.shicimingju.com' + oa['href']
        # print(href)
        # exit()
        #向href发起请求，解析响应，得到内容
        text = get_string(href)
        #写入文件
        fp.write(title + '\n' + text)
        print("结束下载----%s" % title)
        time.sleep(2)
    fp.close()



def main():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    #构建请求对象
    request = get_request(url)
    #得到响应
    content = get_content(request)
    #通过bs4解析网页内容
    parse_content(content)

if __name__ == '__main__':
    main()