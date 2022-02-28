import scrapy
import time

class MovieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = ['https://yts.mx/browse-movies?page=1972']

    

    def parse(self, response):
        for movies in response.css('div.browse-movie-wrap'):
            yield {
                'title': movies.css('a.browse-movie-title::text').get(),
                'year' : movies.css('div.browse-movie-year::text').get(),
                'genre' : response.xpath('/html/body/div[4]/div[4]/div/section/div/div[4]/a/figure/figcaption/h4[2]/text()').get(),
                'rating' : movies.css('h4::text').get(),
                'link' : movies.css('a.browse-movie-link').attrib['href']

            }
        
        next_page1 = response.xpath('/html/body/div[4]/div[4]/div/div[1]/ul/li[2]/a').attrib['href']
        

            
        if next_page1 is not None:
            yield response.follow(next_page1, callback=self.parse)
            time.sleep(2)



