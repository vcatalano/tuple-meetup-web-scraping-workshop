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

print(page.content)

# body = soup.find('body')
# the_contents_of_body_without_body_tags = body.findChildren()
# print(the_contents_of_body_without_body_tags)


h1 = soup.find('h1')
header = h1.findChildren()

print(header)
print('The header is: {}' % header)

print('Title:')
print(soup.title)

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
