from selenium import webdriver
import time

url = 'https://movie.douban.com/typerank?type_name=喜剧&type=24&interval_id=100:90&action='
path = r'C:\Users\ADMIN\Desktop\软通python\day6\资料\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#创建浏览器对象
browser = webdriver.PhantomJS(executable_path = path)
browser.get(url)
time.sleep(3)
browser.save_screenshot('./pic/douban1.png')
#模拟滚动条到底部
js = 'document.body.scrollTop=20000'
#phantomjs执行js这个代码
browser.execute_script(js)
time.sleep(10)
browser.save_screenshot('./pic/douban2.png')

#得到执行完js之后的代码
#网页的内容
# browser.page_source
# with open('douban.html','w',encoding='utf8')as fp:
#     fp.write(browser.page_source)
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(browser.page_source)
# #要啥那啥
#
# browser.quit()




