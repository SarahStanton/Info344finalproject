from django.conf.urls import patterns, include, url
from instaSite import views

urlpatterns = [
	url(r'^$', views.home, name='home'),  
	url(r'^location$', views.get_search, name='get_search'),
	url(r'^picture/detail/(?P<pk>\d+)/$', views.picture_detail, name='picture_detail'),
	url(r'^picture/(?P<pk>d+)/$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^category$', views.category_list, name='category_list'),
	
]
