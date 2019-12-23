import requests
import time
from bs4 import BeautifulSoup
import re,json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
def parse_first_page(url):
    #处理一级页面，得到所有的数字，字母开头的链接
    r = requests.get(url=url,headers=headers)
    #生成soup对象
    soup = BeautifulSoup(r.text,'lxml')
    #得到以数字开头的a对象
    number_a_list = soup.select('.bus_kt_r1 > a')
    # print(len(number_a_list))
    #得到以字母开头的a对象
    char_a_list = soup.select('.bus_kt_r2 > a')
    # print(len(char_a_list))
    all_a_list = number_a_list + char_a_list
    all_href_list = []
    #提取所有的链接
    for oa in all_a_list:
        #添加协议主机
        href_url = url.rstrip('/')+oa['href']
        all_href_list.append(href_url)
    return all_href_list

def parse_second_page(all_href_list,url,fp):
    #遍历这个里面，依次发送请求
    for href in all_href_list:
        r = requests.get(url=href,headers=headers)
        soup = BeautifulSoup(r.text,'lxml')
        #提取详细公交的链接
        odiv = soup.find('div',id='con_site_1')
        #查找div下的所有a链接
        oa_list = odiv.find_all('a')
        #提取所有a对象的href
        oa_href_list = []
        for oa in oa_list:
            href = url.rstrip('/') + oa['href']
            oa_href_list.append(href)
        # print(len(oa_href_list))
        # exit()
        #向三级页面发送请求，一次提取数据
        parse_third_page(oa_href_list,fp)

def parse_third_page(oa_href_list,fp):

    for href in oa_href_list:
        r = requests.get(url=href,headers=headers)
        soup = BeautifulSoup(r.text,'lxml')
        #线路名称
        route_name = soup.select('.bus_i_t1 > h1')[0].text
        print("开始抓取%s......" % route_name)
        #运行时间
        run_time = soup.select('.bus_i_content > .bus_i_t4')[0].string.lstrip('运行时间：')
        #票价信息
        price_info = soup.select('.bus_i_content > .bus_i_t4')[1].string.lstrip('票价信息：')
        #公交公司
        bus_company = soup.select('.bus_i_content > .bus_i_t4 > a')[0].string
        #上行总站数，正则提取
        # up_total= re.compile(r'<span class="bus_line_no">.*?(\d+).*</span>')
        # ret = up_total.findall(r.text)
        # print(ret[0])
        # exit()
        up_total = soup.select('.bus_line_top > span ')[0].string.strip('共站').strip()
        #获取上行总站牌
        # up_total_name = soup.select('.bus_site_layer > div > a')
        up_div = soup.select('.bus_site_layer')[0]
        up_total_list = up_div.select('div > a')
        up_name_list = []
        #遍历，获取所有名字
        for oa in up_total_list:
            up_name_list.append(oa.string)

        try:
            #下行总站数
            down_total = soup.select('.bus_line_top > span ')[1].string.strip('共站').strip()
            #获取下行总站牌
            down_div = soup.select('.bus_site_layer')[1]
            down_total_list = down_div.select('div > a')
            down_name_list = []
            # 遍历，获取所有名字
            for oa in down_total_list:
                down_name_list.append(oa.string)
        except Exception as e:
            down_total = "无下行线路"
            down_name_list = []

        #保存到字典中
        item = {
            '线路名称':route_name,
            '运行时间':run_time,
            '票价信息':price_info,
            '公交公司':bus_company,
            '上行总站数':up_total,
            '上行总站牌':up_name_list,
            '下行总站数':down_total,
            '下行总站牌':down_name_list
        }

        string = json.dumps(item,ensure_ascii=False)
        fp.write(string + '\n')
        print("结束抓取%s......"%route_name)
        time.sleep(2)


def main():
    url = 'https://xian.8684.cn/'
    fp = open('西安公交.txt','w',encoding='utf8')
    #解析一级节点
    all_href_list = parse_first_page(url)
    #解析二级节点
    parse_second_page(all_href_list,url,fp)

if __name__ == '__main__':
    main()