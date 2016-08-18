import json 
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response
from social.backends.oauth import BaseOAuth1, BaseOAuth2

from django.apps import AppConfig
from .models import Picture, Category, User
from .forms import CategoryForm, SearchForm
import tweepy
from tweepy.auth import OAuthHandler
import requests


from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.contrib.auth import views as auth_views



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

#
##	def home(request):
#	 Home view, displays login mechanism
#	if request.user.is_authenticated():
#		return redirect('done')
#	return context()



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


def picture_list(request):
	"""
	category_name = category_url.replace(category_url, '_', ' ')
	context_dict = {'category_name': category_name}
	try: 
		category = Category.objects.get(folder=category_name)
		picture = Picture.objects.filter(category=category)
		context_dict['picture'] = picture
		context_dict['category'] = category
	except:
		pass
	"""
	pictures = Picture.objects.filter(category=2)
	return render(request, 'instaSite/picture_list.html', {'pictures': pictures})



def home(request):

	context = RequestContext(request, {'request': request,'user': request.user})

	return render_to_response('instaSite/home.html',context_instance=context)



def get_search(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.save(commit=False)
			search.topic = form.cleaned_data['topic']
			search.save()

			
			#return redirect('results', pk=search.pk)

			#search = Search.objects.get(pk=pk)
			api = get_api(request)
			#for x in range(0, 3):
			results = api.search(search.topic, count=100)
			tweets_images=[]
			for i in results:
				try:
					if i.entities['media'][0]['type']=='photo':
						tweets_images.append({'url':i.entities['media'][0]['media_url'],'id':i.id})
						id_images.append(i.id)
				except:
					pass
			return render(request, 'instaSite/result_list.html', {'results': tweets_images})


	else:
		form = SearchForm()
	return render(request, 'instaSite/location.html', {'form': form})
		
'''
def results(request, pk):
	search = Search.objects.get(pk=pk)
	api = get_api(request)
	#for x in range(0, 3):
	results = api.search(search, count=100)
	tweets_images=[]
	for i in results:
		try:
			if i.entities['media'][0]['type']=='photo':
				tweets_images.append({'url':i.entities['media'][0]['media_url'],'id':i.id})
				id_images.append(i.id)
		except:
			pass
	return render(request, 'instaSite/result_list.html', {'results': tweets_images})
'''

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

