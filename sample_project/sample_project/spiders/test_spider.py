# -*- coding: utf-8 -*-
import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://http://books.toscrape.com//']

    def parse(self, response):
        pass
