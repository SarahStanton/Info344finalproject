from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Picture, Search, User

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('folder', 'user')

class PictureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Picture
		fields = ('primary', 'link', 'category', 'search')

class SearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Search
		fields = ('topic')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'accessToken', 'accessSecret')


