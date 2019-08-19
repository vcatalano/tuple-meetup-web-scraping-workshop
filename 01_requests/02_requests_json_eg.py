import requests
import pprint

""" Requests Library JSON Example:

Using the requests library, you can view contents in other formats as well. 
One very popular data format for the web is JSON (JavaScript Object Notation).
With the Requests library, you can easily read in JSON data to a dictionary.

Pro tip! Many times you don't even need web scraping. Numerous websites 
provide the information you may be looking for through the use of APIs.

(https://www.json.org/)
(https://2.python-requests.org/en/master/)

"""

# Try replacing this URL with different ones and see what you get!
#
#  https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
#  https://xkcd.com/353/info.0.json
#
#  Pro tip: try replacing "black-mirror" with other episodes

r = requests.get('http://api.tvmaze.com/singlesearch/shows?q=black-mirror&embed=episodes')

print('JSON:')

# We use the `pprint` library to make the object easier to read
pprint.pprint(r.json())

# What happens when we output r.text?
