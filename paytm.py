from lxml import html
from bs4 import BeautifulSoup
import requests


class paytm:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		#self.depth = depth
		#self.pro = []

	def crawl(self):
		
		return self.product_data(self.starting_url)

	def product_data(self,link):
		start_page = requests.get(link)
		soup=BeautifulSoup(start_page.text,'html.parser')		
#tree = html.fromstring(start_page.text)
		
		name = soup.find(class_ ="NZJI").text
		price = soup.find(class_="_2CNI").text
		rating = soup.find(class_="_2Q8k").text
		#reviews = tree.xpath('//div[@class="head"]/text()')[0]
		
		
						
		return Product(name,price,rating)


class Product:

	def __init__(self, name, price, rating):
		self.name = name
		self.price = price
		self.rating = rating
		#self.reviews = reviews

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\n rating: "+self.rating.encode('UTF-8')+ "\r\n")
links = [
	'https://paytm.com/shop/p/sony-kdl-43w800d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WBEST182943E8D29DD4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|1||000000014E57C0E78358939E8F41C4059135CE98|','https://paytm.com/shop/p/lg-43lh576t-108-cm-43-led-tv-full-hd-LARLG-43LH576T-BANG2686178B3F0E0D?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|2||000000014E57C0E78358939E8F41C4059135CE98|',
	'https://paytm.com/shop/p/sony-kdl-43w950d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WSONY2330508D4F73C4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|13||000000014E57C0E78358939E8F41C4059135CE98|'
        ]

for link in links:
	crawler = paytm(link)
	data = crawler.crawl()
	print "name: "+ data.name
	print "price" + data.price
	print "rating"+ data.rating

