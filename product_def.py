# from str import join
import psycopg2
import re

class Product:

	def __init__(self,site, url, name="", price="", description="", key_words="",cat_name="",sub_cat_name="",rating="2.5"):
		self.url = url
		self.site = site
		self.name = name
		p1 = re.findall(r'[0-9]+[\.]*[0-9]*', price)
		self.price = "".join(p1)
		p2 = re.findall( r'[0-9\.]+',rating)
		self.rating = "".join(p2)
		self.description= description.replace("'","&#39;")
		self.key_words=key_words
		self.cat_name= cat_name
		self.sub_cat_name= sub_cat_name

		#self.product_id= id

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\nRating: "+ self.rating.encode('UTF-8') + "\r\nDescription: "+ self.description.encode('UTF-8') + "\r\nKey_words: "+ self.key_words.encode('UTF-8') + "\r\n" )
	def save(self):
		try:
			conn = psycopg2.connect("dbname='compare_prod' user='postgres' host='localhost' password='Innova123'")
			# print "connected"
		except Exception as e:
			# print "Unable to connect"	
			print e
		cur = conn.cursor()
		query = "SELECT id from compare_app_product where url='%s'" % self.url
		try:
			cur.execute(query)
			rows = cur.fetchall() 
			# print "Checking %s" % self.url
			# print len(rows)
			if len(rows) > 0:
				# print "product exists"
				self.product_id = rows[0][0]
			else:
				# print "product doesnot exists"
				query ="INSERT INTO compare_app_product(url, site, active) VALUES ('%s','%s','%s') RETURNING id" % (self.url, self.site, 1)
				cur.execute(query)
				self.product_id = cur.fetchone()[0]
				# print self.product_id
		except Exception as e:
			# print "connot get the product id"
			print e
		try:
			query = "SELECT id from compare_app_category where name='%s'" % self.cat_name
			if len(rows) > 0:
				# print "category exists"
				self.cat_id = rows[0][0]
			else:
				# print "product doesnot exists"
				query ="INSERT INTO compare_app_category(name) VALUES ('%s') RETURNING id" % (self.cat_name)
				cur.execute(query)
				self.cat_id = cur.fetchone()[0]
				# print self.cat_id


			query = "SELECT id from compare_app_subcategory where name='%s' and category_id ='%s'"% (self.sub_cat_name,self.cat_id)  
			if len(rows) > 0:
				# print "subcategory exists"
				self.sub_cat_id = rows[0][0]
			else:
				# print "subcategory doesnot exists"
				query ="INSERT INTO compare_app_subcategory(name,category_id) VALUES ('%s','%s') RETURNING id" % (self.sub_cat_name,self.cat_id)
				cur.execute(query)
				self.sub_cat_id = cur.fetchone()[0]
				# print self.sub_cat_id
		except Exception as e:
			# print "cannot get sub category id"
			print e

		# cur.execute("select * from products")
		# rows = cur.fetchall()
		# for row in rows:
			print row
		# cur.execute("select * from product_metadata")
		# rows = cur.fetchall()
		# for row in rows:
			print row
		try:
			query = "INSERT INTO compare_app_productmetadata(product_id, name,price,rating,description,key_words,latest,sub_catagory_id)VALUES('%s','%s','%s','%s', '%s','%s','1','%s')" % (self.product_id, self.name, self.price, self.rating,self.description,self.key_words,self.sub_cat_id)
			cur.execute(query)	
		except Exception as e:
			# print "connot execute"
			print e
		conn.commit()


