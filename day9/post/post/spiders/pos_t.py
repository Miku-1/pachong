# -*- coding: utf-8 -*-
import scrapy


class PosTSpider(scrapy.Spider):
    name = 'pos_t'
    allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
