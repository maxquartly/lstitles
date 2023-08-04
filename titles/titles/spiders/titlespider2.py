import scrapy


class Titlespider2Spider(scrapy.Spider):
    name = "titlespider2"
    start_urls = ["https://fhr.ru/news/"]

    def parse(self, response):
            # Get a list of all the div elements with class name "news-list"
            news_list_divs = response.css('div.news-list')

            # Loop through the divs and extract the text from each one
            for div in news_list_divs:
                yield {
                    'text': div.get()
            }
                
                # scrapy crawl titlespider2 -o output2.json