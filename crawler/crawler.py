import requests
from bs4 import BeautifulSoup

response = requests.get('http://website:5000')
soup = BeautifulSoup(response.text, 'html.parser')

print("Crawled content:", soup.get_text())
