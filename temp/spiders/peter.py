# -*- coding: utf-8 -*-
import scrapy
from temp.items import TempItem
from bs4 import BeautifulSoup

class PeterSpider(scrapy.Spider):
    name = 'peter'
    start_urls = ['http://www.mizzimaburmese.com/news/cjnews',
                  'http://www.mizzimaburmese.com/news/regional',
                  'http://www.mizzimaburmese.com/news/technology',
                  'http://www.mizzimaburmese.com/news/local',
                  'http://www.mizzimaburmese.com/news/special',
                  'http://www.mizzimaburmese.com/sports/2018-world-cup',
                  'http://www.mizzimaburmese.com/sports/one-championship',
                  'http://www.mizzimaburmese.com/sports/international',
                  'http://www.mizzimaburmese.com/sports/local',
                  'http://www.mizzimaburmese.com/business/international',
                  'http://www.mizzimaburmese.com/business/domestic',
                  'http://www.mizzimaburmese.com/interview',
                  'http://www.mizzimaburmese.com/opinion/article',
                  'http://www.mizzimaburmese.com/opinion/youth-s-sky',
                  'http://www.mizzimaburmese.com/categories/%E1%80%A1%E1%80%9A%E1%80%BA%E1%80%92%E1%80%AE%E1%80%90%E1%80%AC%E1%80%B7%E1%80%91%E1%80%B6%E1%80%95%E1%80%B1%E1%80%B8%E1%80%85%E1%80%AC',
                  'http://www.mizzimaburmese.com/categories/%E1%80%A1%E1%80%AC%E1%80%98%E1%80%B1%E1%80%AC%E1%80%BA',
                  'http://www.mizzimaburmese.com/consumer-radio',
                  'http://www.mizzimaburmese.com/tv/current-news',
                  'http://www.mizzimaburmese.com/tv/hyper-sport',
                  'http://www.mizzimaburmese.com/tv/tasty-trip',
                  'http://www.mizzimaburmese.com/tv/business',
                  'http://www.mizzimaburmese.com/tv/women',
                  'http://www.mizzimaburmese.com/tv/meet-the-successful',
                  'http://www.mizzimaburmese.com/category/farmers',
                  'http://www.mizzimaburmese.com/election2015/dialogue',
                  'http://www.mizzimaburmese.com/cartoon',
                  'http://www.mizzimaburmese.com/gallery',
                  'http://www.mizzimaburmese.com/category/%E1%80%9E%E1%80%98%E1%80%AC%E1%80%9D%E1%80%98%E1%80%B1%E1%80%B8%E1%80%92%E1%80%8F%E1%80%BA%E1%80%9C%E1%80%BB%E1%80%B1%E1%80%AC%E1%80%B7%E1%80%95%E1%80%B1%E1%80%AB%E1%80%B7%E1%80%9B%E1%80%B1%E1%80%B8-%E1%80%9B%E1%80%B1%E1%80%92%E1%80%AE%E1%80%9A%E1%80%AD%E1%80%AF%E1%80%A1%E1%80%85%E1%80%AE%E1%80%A1%E1%80%85%E1%80%89%E1%80%BA',
                  'http://www.mizzimaburmese.com/world-news',
                  'http://www.mizzimaburmese.com/entertainment/international',
                  'http://www.mizzimaburmese.com/entertainment/domestic',
                  'http://www.mizzimaburmese.com/health',
                  'http://www.mizzimaburmese.com/health-talk',
                  'http://www.mizzimaburmese.com/health-article',
                  'http://www.mizzimaburmese.com/special-report/meet-the-successful',
                  'http://www.mizzimaburmese.com/special-report/husbandry-sector',
                  'http://www.mizzimaburmese.com/special-report/tasty-trip',
                  'http://www.mizzimaburmese.com/special-report/7-minutes',
                  'http://www.mizzimaburmese.com/special-report/women-in-myanmar-soceity',
                  'http://www.mizzimaburmese.com/special-report/the-best-football-matches',
                  'http://www.mizzimaburmese.com/special-report/tasty-words',
                  'http://www.mizzimaburmese.com/special-report/road-safety',
                  'http://www.mizzimaburmese.com/special-report/weather-forecast',
                  'http://www.mizzimaburmese.com/special-report/2017-Water-Festival']

    def parse(self, response):
        headlineurl=response.xpath('//div[@class="news-category-large-image-image"]/a/@href').extract()
        for hurl in headlineurl:
            yield response.follow(hurl,callback=self.get_news_details)
        smallurl=response.xpath('//div[@class="news-category-small-image-image"]/a/@href').extract()
        for surl in smallurl:
            yield response.follow(surl,callback=self.get_news_details)
        next_page_url=response.css('li.pager-next>a::attr(href)').extract()[0]
        if next_page_url is not None:
            yield response.follow(next_page_url,callback= self.parse)
        else:
            pass

    def get_news_details(self,response):
        item=TempItem()
        item['title']=''.join(response.xpath('//div[@class="news-details"]/div[@class="news-details-title"]/child::text()').extract())
        item['category']=' '.join(response.css('div.news-details-category.color-269>a::text').extract())
        item['pubDate']=response.css('div.news-details-date>span.date-display-single::text').extract()
        item['author']=response.css('div.news-details-author-by::text').extract()
        item['body']=''.join(response.css('div.field-item.even>p::text').extract())
        item['img']="Image Links : "+','.join(response.css('div.news-details-image>img::attr(src)').extract())
        item['ytlink']="Youtube Links"+','.join(response.css('div.field-item.even>iframe::attr(src)').extract())
        yield item
            
