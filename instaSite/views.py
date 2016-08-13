from django.shortcuts import render
from .models import Picture

# Create your views here.
def picture_list(request):
	pictures = Picture.objects.all()
	return render(request, 'instaSite/picture_list.html', {'pictures': pictures})

def hashtag(request):
    return render(request, 'instaSite/hashtag.html', {})

def location(request):
    return render(request, 'instaSite/location.html', {})

