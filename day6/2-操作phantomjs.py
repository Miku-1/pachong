from selenium import webdriver
import time

path = r'C:\Users\ADMIN\Desktop\软通python\day6\资料\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'

#创建浏览器对象
browser = webdriver.PhantomJS(executable_path=path)

url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
#拍个照片记录状态
browser.save_screenshot('./pic/baidu.png')
#打开搜索栏，输入男子汉
browser.find_element_by_id('kw').send_keys('男子汉')
time.sleep(3)
#点击百度一下
browser.find_element_by_id('su').click()
time.sleep(3)
#拍个找照片
browser.save_screenshot('./pic/男子汉.png')
time.sleep(1)
browser.quit()




