from lxml import html
import requests


class Amazon:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		
	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	
	def product_data(self,link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)
		
		name = tree.xpath('//span[@id="productTitle"]/text()')[0]
		price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')[0]
		


		return Product(name, price)

			
		
class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\n" )

links = [	'http://www.amazon.in/Samsung-Galaxy-S5-Shimmery-White/dp/B00JB6RXBI/ref=sr_1_3?ie=UTF8&qid=1488863718&sr=8-3&keywords=samsung+galaxy+s5',
		 'http://www.amazon.in/Apple-iPhone-6s-Gold-16GB/dp/B016QBTCMS/ref=sr_1_12?ie=UTF8&qid=1488806330&sr=8-12&keywords=apple+iphone+6s',
		'http://www.amazon.in/Lenovo-K3NOTE-K3-Note-Black/dp/B01FDMCO44/ref=sr_1_1?s=electronics&ie=UTF8&qid=1488866836&sr=1-1&keywords=lenovo+k3+note']

for link in links:
	crawler = Amazon(link)
	data = crawler.crawl()
	print data	

