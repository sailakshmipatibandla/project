class Product:

	def __init__(self, name="", price="", rating=""):
		self.name = name
		self.price = price
		self.rating = rating

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\nRating: "+ self.rating.encode('UTF-8') + "\r\n" )
