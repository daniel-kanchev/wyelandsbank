import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from wyelandsbank.items import Article


class WyelandsSpider(scrapy.Spider):
    name = 'wyelands'
    start_urls = ['https://www.wyelandsbank.co.uk/news-blog']

    def parse(self, response):
        links = response.xpath('//div[@class="media__content"]//p/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="hero__content"]//h1/text()').get()
        category = response.xpath('//p[@class="article__meta"]//a/text()').get()

        date = response.xpath('//p[@class="article__meta"]//text()').getall()[-1].split()[-1]
        date = datetime.strptime(date, '%d/%m/%Y')
        date = date.strftime('%Y/%m/%d')
        content = response.xpath('//article[@class="column--heaviest article"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content[3:]).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)
        # item.add_value('author', author)
        item.add_value('category', category)
        # item.add_value('tags', tags)

        return item.load_item()

# response.xpath('').get()

