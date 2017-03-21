from compare_app.models import ProductMetadata

result1 = ProductMetadata.objects.filter(name__icontains='iphone')
#stdlogger.debug("Query %s" % str(result1.query))

for i in result1:
	print result1[i].name








