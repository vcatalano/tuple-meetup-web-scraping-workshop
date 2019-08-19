import requests

""" Requests Library Problem:

Now that you are familiar with getting data from a URL, let's try to find 
some important data on a page and download it. This script takes a URL of an
image and will download it to your computer. Using Chrome Developer Tools,
find an image from a website (e.g. https://xkcd.com/) and attempt to download
it.

Extra credit: Can you figure out a way to download multiple images?

"""


# Replace this URL with the URL of the image you want to download
url = '[FIGURE OUT THIS URL]'
filename = 'sample.jpg'

response = requests.get(url)

if response.status_code != 200:
    print('Oops, it looks like I couldn''t load the URL')
    quit()  # Nothing left to do...

# Save the contents of the file to a file
with open(filename, 'wb') as f:
    f.write(response.content)
