# from django.db import models

# # Create your models here.


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


from django.db import models

# Create your models here.


class Product(models.Model):
	url = models.CharField(max_length=1000)
	site =models.CharField(
        max_length=10,
        choices=(('ebay','EBay'),('amazon','Amazon'),('snapdeal','Snapdeal'),('paytm','PayTM')),
        default='ebay',
    )
	active = models.BooleanField(default=True)


class Category(models.Model):
	name = models.CharField(max_length=100)


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# catagory_id = models.IntegerField(default=0)
	name = models.CharField(max_length=100)

class ProductMetadata(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# product_id = models.IntegerField(default=0)
	sub_catagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField("Description", null=True, blank=True)
	key_words = models.CharField(max_length=300)
	price =  models.FloatField(default=0)
	rating = models.DecimalField(max_digits=5, decimal_places=2)
	latest = models.BooleanField(default=True)



# from compare_app.models import Product




# catagorys
# name(string)
# sub catagorys
# catagory_id(int)
# name(string)
# Product Metadata
# product_id(int)
# sub_catagory_id(int)
# name(string)
# description(text)
# key words(string)
# price(integer)
# rating(integer)
# latest(boolean)