# -*- coding: utf-8 -*-
import scrapy


class NewsscraperSpider(scrapy.Spider):
    name = 'newsScraper'
    allowed_domains = ['www.moneycontrol.com']
    start_urls = ['https://www.moneycontrol.com/news/business/stocks/']

    def parseNewsPage(self, response, data):
        newsContent = response.xpath("..//div[@class='content_wrapper arti-flow']//p//text()").extract()
        data["content"] = '\n'.join(newsContent).strip()
        yield data

    def parse(self, response):
        newsRows = response.xpath("..//li[@class='clearfix']")
        for newsRow in newsRows:
            newsTitle = newsRow.xpath("h2//text()").extract_first()
            newsURL = newsRow.xpath("h2//a//@href").extract_first()
            newsdate = newsRow.xpath(".//span//text()").extract_first()
            newsGist = newsRow.xpath(".//p//text()").extract_first()
            data = {
                "title": newsTitle,
                "link": newsURL,
                "date": newsdate,
                "gist": newsGist
            }
            yield scrapy.Request(newsURL, callback=self.parseNewsPage, cb_kwargs=dict(data=data)) 
        nextPage = response.xpath("..//a[@class='last']//@href").extract_first()
        if nextPage:
            absoluteURL = f"https://www.moneycontrol.com{nextPage}"
            yield scrapy.Request(absoluteURL, callback=self.parse)