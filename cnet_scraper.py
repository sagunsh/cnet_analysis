# -*- coding: utf-8 -*-

# Scrapes headlines and published date from cnet.com sitemap
# To run the scraper
# scrapy runspider cnet_scraper.py -o cnet_scraper.csv
# scrapy runspider cnet_scraper.py -o cnet_scraper.json

import scrapy
from scrapy import Request

from dateutil.parser import parse


class CnetScraperSpider(scrapy.Spider):
    name = 'cnet_scraper'
    allowed_domains = ['cnet.com']

    def start_requests(self):
        url = 'https://www.cnet.com/sitemaps/articles/{}/'
        for year in range(1995, 2020):
            yield Request(url.format(year))

    def parse(self, response):
        for news in response.css('ul.items>li.row'):
            yield {
                'title': news.css('a::text').extract_first('').strip(),
                'link': response.urljoin(news.css('a::attr(href)').extract_first()),
                'published_date': parse(news.css('div.date::text').extract_first()).strftime('%Y-%m-%d'),
            }

        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page:
            yield Request(response.urljoin(next_page))
