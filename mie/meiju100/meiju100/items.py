
import scrapy


class Meiju100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    storyName = scrapy.Field()
    storyState = scrapy.Field()
    tvStation = scrapy.Field()
    updateTime = scrapy.Field()

class UrlItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title=scrapy.Field()
    time=scrapy.Field()
    readtimes=scrapy.Field()
    article_url=scrapy.Field()
    pass
   

