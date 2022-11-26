# this package using for all data in this link grap parpuss
import requests
# Beautiful soup using for Scraping data from a site 
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii', 'ignore')
soup = BeautifulSoup( text, 'lxml')
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1:]

for row in rows:
    data = row.find_all(['th','td'])
    try:
        # print(data[0].a.text)
        print(data[-1].text)
    except:
        pass  