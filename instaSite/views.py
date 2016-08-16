from __future__ import absolute_import, print_function
from django.shortcuts import redirect, render
from .models import Picture, Category, User
from .forms import CategoryForm
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import tweepy

CONSUMER_KEY=''
CONSUMER_SECRET=''
'''CALLBACK_URL = set it in my twitter acc to link to http://rparesa.info344.com/ ? '''

session=dict()

def auth(request):
    # start the OAuth process, set up a handler with our details
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, 'http://stants5.info344.com:8888/placeholder/')
    # direct the user to the authentication url
    # if user is logged-in and authorized then transparently goto the callback URL
    auth_url = oauth.get_authorization_url(True)
    response = HttpResponseRedirect(auth_url)
    # store the request token
    #request.session['unauthed_token_tw'] = (oauth.request_token['oauth_token'], oauth.request_token['oauth_token_secret']) 
    #session.set('request_token', oauth.request_token)
    session['request_token']=oauth.request_token
    return response

def callback(request):
    verifier = request.GET.get('oauth_verifier')
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    #token = request.session.get('request_token')
    token = session['request_token']
    # remove the request token now we don't need it
    #request.session.delete('request_token')
    del session['request_token']
    oauth.request_token = token
    try:
        oauth.get_access_token(verifier)
    except tweepy.TweepError:
        print ('Error. Failed to get access token')

    u = User(accessToken=oauth.access_token, accessSecret=oauth.access_token_secret)
    u.save()

  
    response = HttpResponseRedirect(reverse('category_list'))
    return response

def get_api(request):
    # set up and return a twitter api object
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    access_key = request.session['access_key_tw']
    access_secret = request.session['access_secret_tw']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api
def info(request):
    """
    display some user info to show we have authenticated successfully
    """
    #if check_key(request):
    api = get_api(request)
    user = api.me()
    return render_to_response('twitSent/info.html', {'user' : user})
    #else:
    #   return HttpResponseRedirect(reverse('main'))


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


def hashtag(request):
    return render(request, 'instaSite/hashtag.html', {})

def location(request):
	return render(request, 'instaSite/location.html', {})


def logout_view(request):
	logout(request)
	return redirect('login')
'''
def login_view():
	a = flickr_api.auth.AuthHandler()
'''

