import scrapy

from ScrapyStudy.items import ImageItem
from scrapy.http import Request


# 抓总舵的图片
class photoSpider(scrapy.Spider):
    name = 'photo'
    host = ''
    base_url = ''

    # start_urls = ['']

    def start_requests(self):
        # 循环多少页
        for i in range(1, 3):
            url = self.base_url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):

        for item in response.css('h3 a'):
            # 两种情况
            type_a = item.css('[target=_blank]::text').extract_first()
            type_b = item.css('font[color=green]::text').extract_first()
            child_url = ''
            if type_a:
                child_url = item.css('::attr(href)').extract_first()
            elif type_b:
                child_url = item.css('font[color=green]::text').extract_first()
            yield Request(self.host + child_url, self.image_parse)

    def image_parse(self, response):
        images = ImageItem()
        images['image_url'] = response.css('input[data-src]::attr(data-src)').extract()
        images['name'] = response.css('h4::text').extract_first()
        yield images
