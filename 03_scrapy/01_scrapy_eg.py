import scrapy

""" Scrapy Framework Example:

Now we get into some <i>real</i> web scraping. The Scrapy framework 
is a powerful and popular framework that handles the traversal and collection
of data from a website. By having a basic understanding of how web pages are 
structured, you should be able to get up-and-running with Scrapy fairly 
quickly.

In this example, we are taking a look at a website filled with quotes -
http://quotes.toscrape.com/. Using the Scrapy Spider, we will download all
the quotes associated with a tag.
 
(https://scrapy.org/)
(http://quotes.toscrape.com/)
(https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)

Run the following:

scrapy runspider 01_scrapy_eg.py -o quotes.json

"""


class QuotesSpider(scrapy.Spider):

    # The name of the runner - this can be anything, really
    name = 'quotes'

    # These are the URLs you want to start scraping from, feel free to change
    # these URLs and see what happens!
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    # The `parse` function is the key to the Spider class. It can either
    # return a set of data to append to our list quotes, OR, a Request object
    # that will continue to traverse the web site "tree"
    def parse(self, response):

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
