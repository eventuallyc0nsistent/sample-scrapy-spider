# -*- coding: utf-8 -*-
import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
        items = response.css('ol.row li.col-xs-6')
        for item in items:
            yield {
                'title': item.css('.product_pod h3 a::text').extract_first(),
                'price': item.css('.product_pod .product_price .price_color::text').extract_first(),
                'availability': item.css('.product_pod .product_price .availability::text').extract()[1].strip(),
            }
