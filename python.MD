python学习笔记

1.dict字典类型 所有def class 。。。定义的参数均为字典类型 *name必须在**name前ggg

2.环境包管理conda

  conda info -e #显示目前已有的环境
  source activate ‘环境名称’ 切换环境
3.scrapy笔记
 创建工程目录 mkdir scrapyProject
	     cd scrapyProject
 创建工程项目 scrapy startproject meiju100
	     cd meiju100
	     scrapy genspider meiju meijtt.com

   items.py--
	import scrapy

	class Meiju100Item(scrapy.Item):
		storyName = scrapy.Field()
		storyState = scrapy.Field()
		tvStation = scrapy.Field()
		updateTime = scrapy.Field()

   meiju.py--


import scrapy
from meiju100.items import Meiju100Item
 
class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']
 
    def parse(self, response):
        items = []
        subSelector = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for sub in subSelector:
            item = Meiju100Item()
            item['storyName'] = sub.xpath('./h5/a/text()').extract()
            item['storyState'] = sub.xpath('./span[1]/font/text()').extract()
            if item['storyState']:
                pass
            else:
                item['storyState'] = sub.xpath('./span[1]/text()').extract()
            item['tvStation'] = sub.xpath('./span[2]/text()').extract()
            if item['tvStation']:
                pass
            else:
                item['tvStation'] = [u'未知']
            item['updateTime'] = sub.xpath('./div[2]/text()').extract()
            if item['updateTime']:
                pass
            else:
                item['updateTime'] = sub.xpath('./div[2]/font/text()').extract()
            items.append(item)
        return items


pipeline.py--

import time
import sys
#reload(sys)  
#sys.setdefaultencoding('utf8')
#在py3.x下不可用，以下代替
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')可省略


class Meiju100Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today + 'movie.txt'
        with open(fileName,'a') as fp:
#           fp.write(item['storyName'][0].encode("utf8") + '\t' + item['storyState'][0].encode("utf8") + '\t' + item['tvStation'][0] + '\t' + item['updateTime'][0] + '\n')
#str()强转下，可以之后深入了解下write()的用法
	 
            fp.write(str(item['storyName']) + '\t' + str(item['storyState']) + '\t' + str(item['tvStation']) + '\t' + str(item['updateTime']) + '\n')


        return item


settings.py--

#修改ROBOTSTXT_OBEY=0
#添加
ITEM_PIPELINES = {'meiju100.pipelines.Meiju100Pipeline':1}

部署完成后项目目录下运行：
scrapy crawl meiju

项目目录下得到 '日期'movie.txt

模板待研究


