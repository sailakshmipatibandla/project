
import psycopg2



try:
	conn = psycopg2.connect("dbname='projectdb' user='postgres' host='localhost' password='Innova123'")
	print "connected"
except:
	print "Unable to connect"	

# table_name = 'product_metadata'
# temp_file = "'/home/innova/project/final.py'"


# cur = conn.cursor()

# query = """COPY """ + product_metadata + """ FROM """ + temp_file + " WITH NULL AS ''; """

# cursor.execute(query)

	
