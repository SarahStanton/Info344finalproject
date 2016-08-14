from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.category_list, name='category_list'),
	url(r'^hashtag$', views.hashtag, name='hashtag'),
	url(r'^location$', views.location, name='location'),
	url(r'^picture$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	# url(r'^category/(?P<category_name_url>\w+)/$', views.picture_list, name='picture_list'),
]
