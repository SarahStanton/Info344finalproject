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


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from instaSite.serializers import UserSerializer, CategorySerializer, PictureSerializer, SearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view

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
	"""Logs out user"""
	auth_logout(request)
	return render_to_response('instaSite/home.html', {})

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
			string = "#" + search.topic
			results = api.search(string, count=100)
			tweets_images=[]
			for i in results:
				try:
					if i.entities['media'][0]['type']=='photo':
						tweets_images.append({'url':i.entities['media'][0]['media_url'],'id':i.id})
						Picture.objects.create(link=i.entities['media'][0]['media_url'], primary=i.id)
						#Picture.objects.filter(link=i.entities['media'][0]['media_url']).update(id=i.id)
				except:
					pass
			return render(request, 'instaSite/result_list.html', {'results': tweets_images, 'string':string})
	else:
		searchForm = SearchForm()
	return render(request, 'instaSite/location.html', {'searchForm': searchForm})


def picture_detail(request, pk):
	categories = Category.objects.all()
	all_pictures = Picture.objects.all()
	if request.method == "POST":
		form = SaveForm(request.POST)
		if form.is_valid():
			p = Picture.objects.get(primary=pk)
			p.update(category=form.cleaned_data['category'])
			'''
			pictures = form.save(commit=False)
			pictures.category = form.cleaned_data['category']
			pictures.save()
			'''
			return redirect('picture_list', folder=pictures.category)
	else:
		form = SaveForm()
	return render(request, 'instaSite/picture_detail.html', {'form':form, 'categories': categories, 'id':pk})


def picture_list(request, folder):
	pictures = Picture.objects.all()
	results = []
	for i in pictures:
		if i.folder == folder:
			results.append({'url':i.link, 'category':i.category})

	return render(request, 'instaSite/picture_list.html', {'pictures': results})


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
        category = Category.objects.get(pk = pk)
    except Category.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategorySerializer(categorys, many = True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', ])
def api_view(request, format=None):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UsesrSerializer(data = request.data)
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

