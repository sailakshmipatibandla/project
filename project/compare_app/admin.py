

# Register your models here.
from django.contrib import admin

from .models import Product

admin.site.register(Product)


from .models import Category

admin.site.register(Category)

from .models import SubCategory

admin.site.register(SubCategory)

from .models import ProductMetadata

admin.site.register(ProductMetadata)