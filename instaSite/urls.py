from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.picture_list, name='picture_list'),
	url(r'^hashtag$', views.hashtag, name='hashtag'),
	url(r'^location$', views.location, name='location'),
]
