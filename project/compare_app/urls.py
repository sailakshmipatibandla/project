from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

    # url(r'^(?P<name>[0-9]+)/product_metadata$', views.product_metadata, name='product_metadata'),

    # url(r'^(?P<name>[0-9]+)/category/$', views.category, name='category'),
 
    # url(r'^(?P<name>[0-9]+)/sub_category/$', views.sub_category, name='sub_category'),
]