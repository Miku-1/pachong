from bs4 import BeautifulSoup
import re
#生成对象
soup = BeautifulSoup(open('soup_test.html',encoding='utf8'),'lxml')
# print(type(soup))
#soup是一个官方对象，不是字符串，但是打印的时候是字符串
# ret = soup.a
# print(ret)
# print(ret.attrs)
# print(ret.attrs['href'])
# print(ret['href'])
# print(ret.string)

# ret = soup.div
# print(ret)
# print(type(ret.text))
# print(ret.text.replace('\n','').replace('\t',''))
# print(ret.text)
# print('*'*30)
# print(ret.get_text())

# ret =soup.find('a',class_='juyi')
# ret =soup.find('a',id='mu')
# ret =soup.find('div',title='fu')
# print(ret.text)
# print(ret.string)

# odiv =soup.find('div',class_='tang')
# ret = odiv.find('a',class_='juyi')
# print(ret.string)

# ret = soup.find_all('a')
# print(ret)
# print(ret[-3]['href'])

# ret = soup.find_all(['a','li'])
# print(ret)

# ret = soup.find_all('a',class_='bai')
# print(ret)

# ret = soup.find_all('a',limit=2)
# print(ret)

# ret = soup.find_all('a',href = re.compile(r'^www'))
# print(ret)

# ret = soup.select('#qing')
# print(ret)

# ret = soup.select('.bai')
# # print(ret[-1])

# ret = soup.select('.song  .su ')
# print(ret)

ret = soup.select('.song > ul > .su')
print(ret[0].string)