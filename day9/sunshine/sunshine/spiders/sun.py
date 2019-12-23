# -*- coding: utf-8 -*-
import scrapy


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):
        # 获取内容
        content = response.xpath('//div[@class="content"]/span/text()')
        print('*'*50)
        print(len(content))
        print('*' * 50)