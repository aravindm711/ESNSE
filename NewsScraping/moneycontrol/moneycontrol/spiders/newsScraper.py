# -*- coding: utf-8 -*-
import scrapy


class NewsscraperSpider(scrapy.Spider):
    name = 'newsScraper'
    allowed_domains = ['www.moneycontrol.com']
    start_urls = ['https://www.moneycontrol.com/news/business/stocks/']

    def parse(self, response):
        newsRows = response.xpath("..//li[@class='clearfix']")
        for newsRow in newsRows:
            newsTitle = newsRow.xpath("h2//text()").extract_first()
            newsURL = newsRow.xpath("h2//a//@href").extract_first()
            newsdate = newsRow.xpath(".//span//text()").extract_first()
            newsGist = newsRow.xpath(".//p//text()").extract_first()
            yield {
                "title": newsTitle,
                "link": newsURL,
                "date": newsdate,
                "gist": newsGist
            } 