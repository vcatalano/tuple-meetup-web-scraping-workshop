import requests

""" Requests Library Example:




"""

response = requests.get('https://www.pythonforbeginners.com/')
print(response.info())
html = response.read()

print(html)
