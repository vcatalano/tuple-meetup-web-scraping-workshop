import scrapy
from scrapy import Request


""" Scrapy Framework Example:

Now we get into some real web scraping. The Scrapy framework recognizes that
many websites maintain a consistent format with h
 
(https://scrapy.org/)
(http://quotes.toscrape.com/)
(https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)

Run the following:

scrapy runspider 04_scrapy_prob_2.py -o rentals.json

"""


class RentalsSpider(scrapy.Spider):

    MAX_PAGES_COUNT = 30

    name = 'craigslist_retnals'

    allowed_domains = ['craigslist.org']

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

        # Get the common elements on the page that represent a listing
        rentals = response.xpath('//p[@class="result-info"]')

        for rental in rentals:

            # Build a URL of actual page of the listing item
            relative_url = rental.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)

            title = rental.xpath('a/text()').extract_first()
            address = rental.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]

            meta = {
                'URL': absolute_url,
                'Title': title,
                'Address': address
            }

            yield Request(absolute_url, callback=self.parse_page, meta=meta)

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = 'https://tucson.craigslist.org' + relative_next_url

        yield Request(absolute_next_url, callback=self.parse)

    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')

        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())

        compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()

        yield {
            'URL': url,
            'Title': title,
            'Address': address,
            'Description': description,
            'Compensation': compensation,
            'Employment Type': employment_type
        }
