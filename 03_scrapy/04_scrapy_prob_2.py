import scrapy
from scrapy import Request


""" Scrapy Framework Example:

Here's another problem using some totally real-life web scraping. Here, we 
are going to scrape rental housing data on Craigslist so we can run some cool 
analytics on the dataset at another time.
 
(https://scrapy.org/)
(https://tucson.craigslist.org/d/apts-housing-for-rent/search/apa)
(https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)

Run the following:

scrapy runspider 04_scrapy_prob_2.py -o rentals.json

"""


class RentalsSpider(scrapy.Spider):

    name = 'craigslist_retnals'

    # An additional option to prevent us from scraping ALL THE THINGS
    allowed_domains = [
        'craigslist.org'
    ]

    # These are the URLs you want to start scraping from
    start_urls = [
        'https://tucson.craigslist.org/d/apts-housing-for-rent/search/apa'
    ]

    # Provide a limit on the number of requests, we don't want to get in
    # trouble...
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 300
    }

    def parse(self, response):

        # Get the common elements on the page that represent an individual
        # listing
        rentals = response.xpath('XPATH CONTAINER FOR THE RENTAL LIST ITEM')

        for rental in rentals:

            # Build a URL of actual page of the listing item
            relative_url = rental.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)

            title = rental.xpath('XPATH OF THE HREF TITLE').extract_first()

            # This metadata gets passed down to the `parse_rental_page`
            # function and allows you provide some additional information at
            # the list level that you might not have at the individual item
            # level
            meta = {
                'url': absolute_url,
                'title': title
            }

            yield Request(absolute_url, callback=self.parse_rental_page, meta=meta)

        relative_next_url = response.xpath('XPATH OF THE NEXT BUTTON').extract_first()
        absolute_next_url = 'https://tucson.craigslist.org' + relative_next_url

        yield Request(absolute_next_url, callback=self.parse)

    # Parses the information we want from a single rental page
    def parse_rental_page(self, response):

        url = response.meta.get('url')
        title = response.meta.get('title')

        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())
        address = response.css('CSS SELECTOR FOR ADDRESS ELEMENT').extract_first()

        yield {
            'url': url,
            'title': title,
            'description': description,
            'address': address
        }
