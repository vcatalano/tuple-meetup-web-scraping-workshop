from bs4 import BeautifulSoup
import requests

""" Beautiful Soup Library Example:

Using the Beautiful Soup library, let's attempt to pull all quotes from the
http://quotes.toscrape.com/ website. Take a look at the URL structure and see
if you can determine a pattern. Iterate through each of the links and build
a list of quotes
 
(https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
(http://quotes.toscrape.com/)

"""

page = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(page.content, features='html.parser')

# TODO - figure out the best selector to use use and list out all quotes on this page
# Hint: Use `soup.find_all`
