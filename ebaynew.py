from lxml import html
import requests


class ebay:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		#self.depth = depth
		#self.pro = []

	def crawl(self):
		
		return self.product_data(self.starting_url)

	def product_data(self,link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)
		
		name = tree.xpath('//h1[@id="itemTitle"]/text()')[0]
		price = tree.xpath('//span[@id="prcIsum"]/text()')[0]
		#rating = tree.xpath('//span[@class="avrg-rating"]/text()')[0]
		#reviews = tree.xpath('//div[@class="head"]/text()')[0]
		
		
						
		return Product(name,price)


class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		#self.rating = rating
		#self.reviews = reviews

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\n Price: "+ self.price.encode('UTF-8')+ "\r\n rating: "+self.rating.encode('UTF-8')+ "\r\n")
links = [
		'http://www.ebay.com/itm/Sony-KDL48R510C-48-48-Inch-Full-HD-1080p-Smart-LED-TV-2015-Model-Built-in-WiFi-/272501553775?hash=item3f725bba6f:g:Y3oAAOSwNRdX5T30',
		'http://www.ebay.com/itm/LG-43UH6107-43-quot-108-cm-quot-Smart-TV-webOS-3-0-4K-/172444939241?hash=item282684f3e9:g:lOkAAOSwnHZYUTpJ',
		'http://www.ebay.com/itm/TV-SAMSUNG-SMARTV-102cm-3D-Tres-peu-utilise-Offre-a-part-pour-la-XBOX-/222429193933?hash=item33c9d026cd:g:iOEAAOSw4A5YrbOg'
        ]

for link in links:
	crawler = ebay(link)
	data = crawler.crawl()
	print "name: "+ data.name
	print "price" + data.price
	#print "rating"+ data.rating
