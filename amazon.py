
from bs4 import BeautifulSoup
from requests import get
import sys
import csv

keywords = sys.argv
url = 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords='
f = csv.writer(open('amazon_results.csv', 'w'))
# f.writerow(['Title', 'Price', 'Rate', 'Img_Url'])

for idx, keyword in enumerate(keywords):
	if idx != 0:
		if idx+1 != len(keywords):
			url = url + keyword + '+'
		else:
			url = url + keyword

source = get(url, headers={"User-Agent":"Defined"}).text

soup = BeautifulSoup(source, 'lxml')

# f.writerow(soup)

for item in soup.find_all('li', class_='s-result-item'):
	if item['id'] != 's-result-list-layout-placeholder':
		print(item['id'])
		img_url = item.find('a', class_='a-link-normal a-text-normal').img['src']
		
		title = item.find('h2', class_='s-access-title').text
		
		price = str(item.find('span', class_='sx-price-whole').text) + ',' + str(item.find('sup', class_='sx-price-fractional').text)

		rate = 'No Rate'
		
		if item.find('i', class_='a-icon-star'):
			rate = item.find('i', class_='a-icon-star').span.text

		f.writerow([item['id'], title, price, img_url, rate])






