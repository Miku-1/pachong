# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):
        # print("*"*50)
        # print(response.text)
        # print("*" * 50)
        div_list = response.xpath('//div[@id="content-left"]/div')
        # print("*"*50)
        # print(len(div_list))
        # print("*" * 50)
        items = []
        for odiv in div_list:
            #头像
            user_face = odiv.xpath('./div//img/@src')[0].extract()
            #用户名
            user_name = odiv.xpath('./div//h2/text()')[0].extract()

            item = {
                '头像':user_face,
                '用户名':user_name
            }
            items.append(item)
        return items
