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

