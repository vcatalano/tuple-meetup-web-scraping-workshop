import requests

""" Requests Library HTML Example:

Using the requests library, you can view the HTML contents of a given page. 
Here, we are printing some information about the Python for Beginners web 
page. 
 
(https://2.python-requests.org/en/master/)

"""

# Try replacing this URL with different ones and see what you get!
r = requests.get('https://www.pythonforbeginners.com/')

print('Status code:')
print(r.status_code)

print('Headers:')
print(r.headers['content-type'])

print('Encoding:')
print(r.encoding)

print('HTML:')
print(r.text)
