import scrapy
class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # 与itcast.py 定义的一一对应
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()