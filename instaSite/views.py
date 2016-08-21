import json 
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response

from django.apps import AppConfig
from .models import Picture, Category, User, Search
from .forms import CategoryForm, SearchForm, SaveForm
import tweepy
from tweepy.auth import OAuthHandler
import requests
import rest_framework

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import viewsets


from django.contrib.auth.models import User, Group
#from ratelimit.decorators import ratelimit
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from instaSite.serializers import UserSerializer, CategorySerializer, PictureSerializer, SearchSerializer
auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY , settings.SOCIAL_AUTH_TWITTER_SECRET)
session = {}
access_token = ''
access_token_secret = ''

def auth(request):
	auth_url = oauth.get_authorization_url(True)
	response = HttpResponseDirect(auth_url)
	session['request_token'] = auth.request_token 
	return response

def callback(request):
	verifier = request.GET.get('oauth_verifier')
	token = request['request_token']
	acces_token = token
	del_session['request_token']
	auth.request_token = token
	try:
		auth.get_access_token(verifier)
	except tweepy.TweepError:
		print(error)
	u = User(accessToken=auth.access_token,accessSecret = auth.access_token_secret)
	session['access_token'] = auth.access_token
	session['access_token_secret'] = auth.access_token_secret
	u.save()
	response = HttpResponseRedirect(reverse('/'))
	return response

def get_api(request):
	auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY , settings.SOCIAL_AUTH_TWITTER_SECRET)
	r_token = session.get('access_token')
	r_secret = session.get('access_token_secret')
	auth.set_access_token(r_token, r_secret)
	api = tweepy.API(auth)
	return api


def logout(request):
	auth_logout(request)
	return redirect('/')

def create_user(self, email=None, password=None):
	user.save()
	return user


def done(request):
	"""Login complete view, displays user data"""
	return context()

# Create your views here.

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'instaSite/category_list.html', {'categories': categories})


def category_new(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.folder = form.cleaned_data['folder']
			category.save()
			return redirect('category_list')
	else:
		form = CategoryForm()
	return render(request, 'instaSite/category_new.html', {'form': form})

def home(request):
	context = RequestContext(request, {'request': request,'user': request.user})

	return render_to_response('instaSite/home.html',context_instance=context)





def get_search(request):
	if request.method == "POST":
		searchForm = SearchForm(request.POST)
		if searchForm.is_valid():
			search = searchForm.save(commit=False)
			search.topic = searchForm.cleaned_data['topic']
			search.save()
		
			#search = Search.objects.get(pk=pk)
			api = get_api(request)
			#for x in range(0, 3):
			strings = '#' + search.topic
			results = api.search(q=strings, count=100)
			tweets_images=[]
			for i in results:
				try:
					if i.entities['media'][0]['type']=='photo':
						p = Picture.objects.create(link=i.entities['media'][0]['media_url'])
						tweets_images.append({'url':i.entities['media'][0]['media_url'], 'id': p.id})
						#Picture.objects.filter(link=i.entities['media'][0]['media_url']).update(id=i.id)
				except:
					pass
			return render(request, 'instaSite/result_list.html', {'results': tweets_images, 'string': strings})
	else:
		searchForm = SearchForm()
	return render(request, 'instaSite/location.html', {'searchForm': searchForm})


def picture_detail(request, pk):
	categories = Category.objects.all()
	all_pictures = Picture.objects.all()
	if request.method == "POST":
		form = SaveForm(request.POST)
		if form.is_valid():
			p = Picture.objects.filter(id=pk)
			p.update(category=form.cleaned_data['category'])
			'''
			pictures = form.save(commit=False)
			pictures.category = form.cleaned_data['category']
			
			p.save()
			'''
			temp = Picture.objects.get(pk=pk)
			temp2 = temp.category_id
			return redirect('picture_list', pk=temp2)
	else:
		form = SaveForm()
	return render(request, 'instaSite/picture_detail.html', {'form':form, 'categories': categories, 'folderid':pk})


def picture_list(request, pk):
	pictures = Picture.objects.filter(category=pk)
	return render(request, 'instaSite/picture_list.html', {'pictures': pictures})


def picture_add(request):
	if request.method == "POST":
		form = PictureForm(request.POST)
		if form.is_valid():
			picture = form.save(commit=False)
			category.folder = form.cleaned_data['picture']
			category.save()
			return redirect('results')
		else:
			form = PictureForm()
	return render(request, 'instaSite/category_new.html', {'form': form})


def main(request):
	return render(request, 'instaSite/home.html', {})


'''
def logout(request):
	logout(request)
	return redirect('info')


def login_view():
	a = flickr_api.auth.AuthHandler()

'''


@api_view(['GET', 'DELETE', ])
def category_api(request, pk, format=None):
	try:
		category = Category.objects.get(pk=pk)
	except Category.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = CategorySerializer(categorys, many=True)
		return Response(serializer.data)
	elif request.method == 'DELETE':
		catagory.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
	else:
		return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', ])
def api_view(request, format=None):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
	else:
		return Response(status = status.HTTP_400_BAD_REQUEST)




class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class PictureViewSet(viewsets.ModelViewSet):
	queryset = Picture.objects.all()
	serializer_class = PictureSerializer

class SearchViewSet(viewsets.ModelViewSet):
	queryset = Search.objects.all()
	serializer_class = SearchSerializer

