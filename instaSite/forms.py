from django import forms

from .models import Category, Picture, Search

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('folder',)

class SearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = ('topic',)


class SaveForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ('link', 'category',)

