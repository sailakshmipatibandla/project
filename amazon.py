# from lxml import html
from bs4 import BeautifulSoup
import requests
from product_def import Product
class Amazon:

	def __init__(self, starting_url):
		self.starting_url = starting_url

	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	def product_data(self,link):
		start_page = requests.get(link)
		# tree = html.fromstring(start_page.text)
		
		# name = tree.xpath('//h1[@id="itemTitle"]/text()')[0]
		# price = tree.xpath('//span[@id="prcIsum"]/text()')[0]
		# description = tree.xpath('//div[@class="itemAttr"]/text()')[0]

		#print "Name: " + name
		#print "Price: " + price

		soup = BeautifulSoup(start_page.text, 'html.parser')
		try:
			name = soup.find('span', id="productTitle").text
			p = soup.find('span', id="priceblock_ourprice")
			if p :
				price = p.text
			else:
				price = soup.find('tr', id="priceblock_saleprice_row").text
			description = ""
			for desc in soup.find_all('div', id="productDescription"):
				description += desc.text 
			
			for tag in soup.find_all("meta"):
				if tag.get("name", None) == "keywords":
					key_words = tag.get("content", None)
					# print key_words
			cat_name = soup.find('a',class_="a-link-normal a-color-tertiary").text
			sub_cat_name = soup.find('a',class_="a-link-normal a-color-tertiary").text	
			return Product("amazon",self.starting_url,name,price, description,key_words,cat_name,sub_cat_name)
		except Exception as e:
			print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			print self.starting_url
			print start_page.text
			print e
			print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"



			
