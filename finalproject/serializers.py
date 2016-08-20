from django.contrib.auth.models import User
from instaSite.models import Category, Picture, Search, User
from rest_framework import serializers

class CategorySerialier(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('folder', 'user')

class PictureSerialier(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Picture
		fields = ('primary', 'link', 'category', 'search')

class SearchSerialier(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Search
		fields = ('topic')

class UserSerialier(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'accessToken', 'accessSecret')
