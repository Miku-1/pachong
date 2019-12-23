# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月22日 下午12:42
    @File   : 二级页面url.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver
import time
from lxml import etree

url = 'https://live.kuaishou.com/v/hot/'
path = r'E:\Python\pachong\day6\资料\ziliao\chromedriver.exe'
#创建浏览器对象
browser = webdriver.Chrome(executable_path = path)
browser.get(url)
time.sleep(3)
#模拟滚动条到底部
js="var q=document.documentElement.scrollTop=10000"
#phantomjs执行js这个代码
browser.execute_script(js)
time.sleep(8)
browser.execute_script(js)
time.sleep(8)
browser.execute_script(js)
time.sleep(8)
html =etree.HTML( browser.page_source)
urllist = html.xpath('//div[@class="video-card video-item"]/a/@href')
print(len(urllist))
browser.quit()




