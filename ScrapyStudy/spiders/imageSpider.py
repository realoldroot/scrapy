import scrapy

from ScrapyStudy.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImageItem()
        item['image_url'] = response.css('.post img::attr(src)').extract()
        item['name'] = response.css('.post-title a::text').extract_first()
        yield item
