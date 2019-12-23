# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):
        print('*' * 50)
        print(response.text)

