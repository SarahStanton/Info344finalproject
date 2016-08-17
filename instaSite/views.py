import json 

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response
from social.backends.oauth import BaseOAuth1, BaseOAuth2

from django.apps import AppConfig
from .models import Picture, Category
from .forms import CategoryForm
import tweepy
import requests


from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from django.contrib.auth import views as auth_views

from django.core.urlresolvers import reverse

def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return redirect('/')

def create_user(self, email=None, password=None):
	user.save()
	return user 

def home(request):
	""" Home view, displays login mechanism"""
	if request.user.is_authenticated():
		return redirect('done')
	return context()



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
	context = RequestContext(request,{'request': request,'user': request.user})
	return render_to_response('instaSite/home.html',context_instance=context)

def location(request):
	return render(request, 'instaSite/location.html', {})

def main(request):
	return render(request, 'instaSite/home.html', {})


'''
def logout(request):
	logout(request)
	return redirect('info')


def login_view():
	a = flickr_api.auth.AuthHandler()
'''

