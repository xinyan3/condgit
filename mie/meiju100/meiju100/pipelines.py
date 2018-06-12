# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import sys
import importlib
importlib.reload(sys)
 
 
class Meiju100Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today + 'movie.txt'
        with open(fileName,'a') as fp:
            fp.write(str(item['storyName']) + '\t' + str(item['storyState']) + '\t' + str(item['tvStation']) + '\t' + str(item['updateTime']) + '\n')

        return item
