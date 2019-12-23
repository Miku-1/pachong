# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):

    # def open_spider(self,spider):
    #     self.file = open('qiubai.txt','w')
    #
    # def close_spider(self,spider):
    #     self.file.close()

    def process_item(self, item, spider):
        self.file = open('qiubai.txt', 'w')
        self.file.write(item + '\n')
        return item

