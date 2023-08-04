import scrapy


class Titlespider4Spider(scrapy.Spider):
    name = "titlespider4"

    start_urls = ["https://news.sportbox.ru"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'DOWNLOAD_DELAY': 2,  # Add a delay of 2 seconds between requests
    }

    def parse(self, response):
            yield {
                'text': response.css('a.b-actually__item').getall()
            }