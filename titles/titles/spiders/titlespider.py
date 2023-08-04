import scrapy

class TitlespiderSpider(scrapy.Spider):
    name = "titlespider"
    start_urls = ['https://m.sports.ru/news/'] # this is the website esp

    def parse(self, response):
        
        #response.css('div.b-news-list__container')


        yield {
            'text' : response.css('div.b-news-list__container').getall()
        }



            #scrapy crawl titlespider8 -o output8.json
