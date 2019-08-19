import requests
import re

""" Requests Library Problem:

Extra credit!

Now that you are familiar with getting data from a URL, let's try to find 
some important text information on a web page. Using a regular expression
(regex), let's try to find some specific metadata on the page. Try to find 
the comic title above the image on the page. (this one is tricky).

Tips: Use `View Source` on Chrome and a Regex tester (https://regex101.com/)

"""


r = requests.get('https://xkcd.com/')

regex = r'<div id=\"ctitle\">(.+?)<\/div>'
pattern = re.compile(regex)

match = re.search(pattern, r.text)

try:
    comic_title = match.group(1)
    print(comic_title)
except:
    print('Could not find a match for the title')
