from django.shortcuts import redirect, render
from .models import Picture, Category
from .forms import CategoryForm
import requests

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

