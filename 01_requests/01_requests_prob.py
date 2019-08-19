import requests

""" Requests Library Problem:




"""

response = requests.get('https://www.pythonforbeginners.com/')
print(response.info())
html = response.read()

print(html)
