from bs4 import BeautifulSoup
import requests

""" Beautiful Soup Library Example:

Using the Beautiful Soup library, let's attempt to pull in some useful 
information from a page. Here, we should try and pull in all quotes from
http://quotes.toscrape.com/.
 
(https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
(http://quotes.toscrape.com/)

"""

page = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(page.content, features='html.parser')

# TODO - figure out the best selector to use use and list out all quotes on this page
# Hint: Use `soup.find_all`
