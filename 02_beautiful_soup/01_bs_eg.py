from bs4 import BeautifulSoup
import requests

""" Beautiful Soup Library Example:

Using the Beautiful Soup library, you can essentially "query" data from the 
web page. This structure is known as the DOM (Document Object Model).
 
(https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
(http://quotes.toscrape.com/)

"""

page = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(page.content, features='html.parser')

print('Page content:')
print(page.content)

h1 = soup.find('h1')
header = h1.findChildren()

print('The header is: {}' % header)

print('Title:')
print(soup.title)

print('Title element name:')
print(soup.title.name)

print('Title element contents:')
print(soup.title.string)

print('All links for the page:')
for link in soup.find_all('a'):
    print(link)

