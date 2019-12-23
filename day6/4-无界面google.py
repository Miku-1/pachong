from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'C:\Users\ADMIN\Desktop\软通python\day6\资料\ziliao\chromedriver.exe'
#创建谷歌浏览器对象
browser = webdriver.Chrome(executable_path = path,chrome_options=chrome_options)

browser.get('http://www.baidu.com/')
time.sleep(3)
browser.save_screenshot('./pic/google.png')
browser.quit()




