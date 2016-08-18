from django.conf.urls import patterns, include, url
from instaSite import views

urlpatterns = [
	url(r'^category$', views.category_list, name='category_list'),
	url(r'^$', views.home, name='home'),  
	url(r'^location$', views.get_search, name='get_search'),
	#url(r'^results$', views.results, name='results'),
	url(r'^picture$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^logout$', views.logout, name='logout'),
	
]
