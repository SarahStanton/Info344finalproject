from django.db import models


# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=100, null=True)
	accessToken = models.CharField(max_length=300, null=True)
	accessSecret = models.CharField(max_length=300, null=True)

	def __str__(self):
		return self.username    

class Category(models.Model):
	folder = models.CharField(max_length=100, null=True)
	user = models.ForeignKey(User, null=True)
	
	def __str__(self):
		return self.folder

class Search(models.Model):
	topic = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.topic

class Picture(models.Model):
	primary = models.IntegerField(null=True)
	link = models.URLField(max_length=300, null=True)
	category = models.ForeignKey(Category, null=True)
	search = models.ForeignKey(Search, null=True)

	def __str__(self):
		return self.link