import scrapy


class Titlespider8Spider(scrapy.Spider):
    name = "titlespider8"
    start_urls = ["https://www.hcsochi.ru/media/news/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'DOWNLOAD_DELAY': 2,  # Add a delay of 2 seconds between requests
    }

    def parse(self, response):
        titles = response.css('div.news-items')
        yield {
            'text' : titles.css('a.news-item__title').get()
        }

#scrapy crawl titlespider8 -o output8.json