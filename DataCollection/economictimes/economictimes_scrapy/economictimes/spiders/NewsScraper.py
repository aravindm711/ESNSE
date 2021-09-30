# -*- coding: utf-8 -*-
import scrapy
import re

class NewsscraperSpider(scrapy.Spider):
    name = 'NewsScraper'
    allowed_domains = ['www.economictimes.indiatimes.com']
    start_urls = ['']

    def __init__(self, filename=None):
        super().__init__()
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        newsContent = response.xpath("..//div[@class='artText']//text()").extract()
        newsTitle = response.xpath("..//h1//text()").extract_first()
        newsDate = response.xpath("..//time//text()").extract_first().split(": ")[1]
        newsGist = response.xpath("..//h2[@class='summary']//text()").extract_first()
        newsURL = response.url

        yield {
            "title": newsTitle,
            "link": newsURL,
            "date": newsDate,
            "gist": newsGist,
            "content": re.sub(' +', " ", ''.join(newsContent).strip())
        }
        