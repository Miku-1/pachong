# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月22日 上午10:21
    @File   : 快手短视频爬取.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests
from selenium import webdriver
import time
from lxml import etree

def get_url(url):
    url = 'https://live.kuaishou.com/v/hot/'
    path = r'E:\Python\pachong\day6\资料\ziliao\chromedriver.exe'
    # 创建浏览器对象
    browser = webdriver.Chrome(executable_path=path)
    browser.get(url)
    time.sleep(3)
    # 模拟滚动条到底部
    js = "var q=document.documentElement.scrollTop=10000"
    # phantomjs执行js这个代码
    browser.execute_script(js)
    time.sleep(5)
    # browser.execute_script(js)
    # time.sleep(8)
    html = etree.HTML(browser.page_source)
    urllist = html.xpath('//div[@class="video-card video-item"]/a/@href')
    browser.quit()
    url_list = ['https://live.kuaishou.com' + i for i in urllist]
    return url_list


def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    get_info(response)


def get_info(response):
    tree = etree.HTML(response.text)
    # 用户名
    username = tree.xpath('//div[@class="profile-user"]/div[@class="profile-user-info"]/div/a/text()')[0].strip()
    # 头像链接
    icon_href = tree.xpath('//div[@class="profile-user"]/div[@class="profile-user-info"]/div/a/img/@src')[0]
    # 视频描述信息
    video_info = tree.xpath('//div[@class="profile-user"]/div[@class="profile-user-desc"]/span/text()')[0]

    video_play_info = tree.xpath('//div[@class="profile-user-count-info"]/span/text()')
    # 播放量,
    watching_count = video_play_info[0]
    # 点赞数(红心数量)
    like_count = video_play_info[1]
    # 评论数
    comment_count = tree.xpath('//div[@class="comment-con"]/div/text()')
    # 视频文件
    print(username,'\n',icon_href,video_info,watching_count,like_count)


def main():
    url = 'https://live.kuaishou.com/v/hot'
    url_list = get_url(url)
    for href in url_list:
        # print(href)
        get_response(href)

if __name__ == '__main__':
    main()