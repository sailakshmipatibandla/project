from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Product,ProductMetadata

def index(request):
	# product = get_object_or_404(Product,pk=product_id)
	#return HttpResponse("Hello, You're looking at url and product_id %s." % (product.url))
	# results = []
	# try:
	# 	results = ProductMetadata.objects.filter(name__icontains=request.GET["Name"],latest=1)
	# except Exception as e:
	# 	print e
	return render(request, 'compare_app/index.html')

	# return render(request, 'compare_app/detail.html', {'product': product})
def search (request):
	results = []
	try:
		results = ProductMetadata.objects.filter(name__icontains=request.GET["search"],latest=1)
	except Exception as e:
		print e
	return render(request, 'compare_app/boot.html', {'results': results})

def product_metadata(request,name):
	results = ProductMetadata.objects.filter(name__icontains='iphone')
	#return HttpResponse("You're looking at product details %s." % (name))
	return render(request, 'compare_app/results.html', {'results': results})

def category(request, name):
	response = "You're looking at the category of the product %s."
	return HttpResponse(response % name)

def sub_category(request, name):
	return HttpResponse("You're looking at sub categories %s." % (name))


