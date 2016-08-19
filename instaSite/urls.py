from django.conf.urls import patterns, include, url
from instaSite import views
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categorys', views.CategoryViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'searchs', views.SearchViewSet)


urlpatterns = [
	url(r'^category$', views.category_list, name='category_list'),
	url(r'^$', views.home, name='home'),  
	url(r'^location$', views.get_search, name='get_search'),
	url(r'^picture/detail/(?P<pk>\d+)/$', views.picture_detail, name='picture_detail'),
	url(r'^picture$', views.picture_list, name='picture_list'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^api/', include(router.urls)),
	url(r'^api/project/$', views.api_view, name='api_view'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
]
