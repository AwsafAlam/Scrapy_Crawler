import scrapy

class WordScraper(scrapy.Spider):

    # name = "quotes"

    # def start_requests(self):
    #     urls = [
    #             'http://quotes.toscrape.com/page/1/',
    #             'http://quotes.toscrape.com/page/2/']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    name = "quotes"
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'http://quotes.toscrape.com/page/4/',
        'http://quotes.toscrape.com/page/5/',
        'http://quotes.toscrape.com/page/6/',
        'http://quotes.toscrape.com/page/7/',
        'http://quotes.toscrape.com/page/8/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
