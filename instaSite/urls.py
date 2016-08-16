from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.category_list, name='category_list'),
	url(r'^hashtag$', views.hashtag, name='hashtag'),
	url(r'^location$', views.location, name='location'),
	url(r'^picture$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^accounts/login/$', views.auth, name='login'),
	url(r'^placeholder/', views.callback, name='callback'),
	url(r'^accounts/logout/$', views.logout_view, name='logout'),
	
]
