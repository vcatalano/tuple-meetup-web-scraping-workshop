import scrapy

""" Scrapy Framework Example:

Now it's your turn! Let's take a look at this fake book sales website and see
if you can get a list of all titles and authors
 
(https://scrapy.org/)
(http://books.toscrape.com/)
(https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)

Run the following:

scrapy runspider 02_scrapy_prob_1_sol.py -o books.json

"""


class BooksSpider(scrapy.Spider):

    # The name of the runner - this can be anything, really
    name = 'books'

    # These are the URLs you want to start scraping from
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):

        # Get all URLs for each book page
        for book_url in response.css('article.product_pod > h3 > a ::attr(href)').extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)

        # Find the link to the next page, if it exists, follow the white rabbit...
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):

        # Get the container element for product information
        product = response.css('div.product_main')
        title = product.css('h1 ::text').extract_first()
        category = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").extract_first()
        description = response.xpath("//div[@id='product_description']/following-sibling::p/text()").extract_first()
        price = response.css('p.price_color ::text').extract_first()

        # Returns the information about a single book as a dictionary
        yield {
            'title': title,
            'category': category,
            'description': description,
            'price': price
        }
