from selenium import webdriver
import time

path = r'C:\Users\ADMIN\Desktop\软通python\day6\资料\ziliao\chromedriver.exe'
#创建谷歌浏览器对象
browser = webdriver.Chrome(executable_path=path)
#通过浏览器上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(2)
#找到输入框往里面输入内容
my_input = browser.find_element_by_id('kw')
#往里面写入内容
my_input.send_keys('动漫')
time.sleep(2)
#找到百度一下按钮
my_button = browser.find_element_by_id('su')
my_button.click()
time.sleep(3)

#点击a链接获取内容
a_href = browser.find_elements_by_xpath('//div[@id="content_left"]/div[2]//a')[0]
a_href.click()
time.sleep(3)   


#浏览器关闭
browser.quit()

'''
browser.find_element_by_id()  根据id查找指定节点
browser.find_element_by_class_name()  根据class查找到指定节点
browser.find_elements_by_xpath()  根据xpath路径查找到指定节点
browser.find_elements_by_css_selector()  根据选择器查找指定节点
browser.find_element_by_link_text()  根据a链接的内容查找指定的a链接
browser.find_elements_by_link_text()  查找多个
'''





