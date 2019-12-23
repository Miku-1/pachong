from lxml import etree
import urllib.request,os,time

class OuMeiSpider(object):
    def __init__(self,start_page,end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.first_url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'
        self.url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv_{}.html'
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',}
    def get_request(self,page):
        #判断使得否为第一页
        if page == 1:
            url = self.first_url
        else:
            url = self.url.format(page)
        #构建请求对象
        request = urllib.request.Request(url=url,headers=self.headers)
        return request

    def parse_content(self,content):
        #生成tree对象
        tree = etree.HTML(content)
        #图片地址
        img_src_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
        # print(len(img_src))
        img_name_list = tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
        #下载图片
        for img_src in img_src_list:
            filename = img_name_list[img_src_list.index(img_src)] + '.' + img_src.split('.')[-1]
            dirname = 'oumei'
            print("正在下载%s-----"%filename)
            filepath = os.path.join(dirname,filename)
            #写入图片
            urllib.request.urlretrieve(img_src,filepath)
            print("结束下载%s-----" % filename)
            time.sleep(2)



    def run(self):
        for page in range(self.start_page,self.end_page+1):
            #拼接地址
            request = self.get_request(page)
            #发送请求得到响应，并且将响应直接转化为内容
            content = urllib.request.urlopen(request).read().decode('utf8')
            #解析内容
            self.parse_content(content)



def main():
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入终止页"))
    obj = OuMeiSpider(start_page,end_page)
    obj.run()

if __name__ == '__main__':
    main()
