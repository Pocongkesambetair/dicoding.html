import requests
from bs4 import BeautifulSoup

url = "https://cookpad.com/id/cari/baked"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())