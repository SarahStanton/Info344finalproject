from django.conf.urls import patterns, include, url
from instaSite import views

urlpatterns = [
	url(r'^category$', views.category_list, name='category_list'),
	url(r'^$', views.home, name='home'),  
	url(r'^location$', views.location, name='location'),
	url(r'^picture$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^logout$', views.logout, name='logout'),
	
]
