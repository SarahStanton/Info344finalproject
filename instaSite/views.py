from __future__ import absolute_import, print_function
from django.shortcuts import redirect, render
from .models import Picture, Category
from .forms import CategoryForm
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

CONSUMER_TOKEN=
CONSUMER_SECRET=
'''CALLBACK_URL = set it in my twitter acc to link to http://rparesa.info344.com/ ? '''

import tweepy
app.route("/")
def send_token():
	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, 
		CONSUMER_SECRET, 
		CALLBACK_URL)

	try: 
		#get the request tokens
		redirect_url= auth.get_authorization_url()
		session['request_token']= (auth.request_token.key,
			auth.request_token.secret)
	except tweepy.TweepError:
		print 'Error! Failed to get request token'

	#this is twitter's url for authentication
	return flask.redirect(redirect_url)	

@app.route("/verify")
def get_verification():

	#get the verifier key from the request url
	verifier= request.args['oauth_verifier']

	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
	token = session['request_token']
	del session['request_token']

	auth.set_request_token(token[0], token[1])

	try:
		    auth.get_access_token(verifier)
	except tweepy.TweepError:
		    print 'Error! Failed to get access token.'

	#now you have access!
	api = tweepy.API(auth)

	#store in a db
	db['api']=api
	db['access_token_key']=auth.access_token.key
	db['access_token_secret']=auth.access_token.secret
	return flask.redirect(flask.url_for('start'))

@app.route("/start")
def start():
	#auth done, app logic can begin
	api = db['api']

	#example, print your latest status posts
	return flask.render_template('tweets.html', tweets=api.user_timeline())

if __name__ == "__main__":
	app.run()
view raw

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

