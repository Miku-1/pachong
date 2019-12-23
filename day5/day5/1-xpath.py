from lxml import etree

tree = etree.parse('xpath.html')
# print(tree)
# ret =tree.xpath('//a[@id="mu"]')
# print(ret[0].text)
# ret = tree.xpath('//div[@class="tang"]/a')
# # print(ret[0].text)

#获取的是属性值
# ret = tree.xpath('//@class')
# print(ret[-1])

# ret = tree.xpath('/div/a[last()]')
# print(ret)

# ret = tree.xpath('//a[contains(text(),"蓦然")]')
# print(ret[0].text)

# ret = tree.xpath('//a[starts-with(@id,"m")]')
# print(ret[0].text)