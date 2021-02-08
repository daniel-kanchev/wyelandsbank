import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    # author = scrapy.Field()
    category = scrapy.Field()
    # tags = scrapy.Field()
