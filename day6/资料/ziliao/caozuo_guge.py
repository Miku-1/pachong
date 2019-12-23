from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(r'E:\Python\pachong\day6\资料\ziliao\chromedriver.exe')

driver.get("http://www.baidu.com")





# 关闭浏览器
driver.quit()