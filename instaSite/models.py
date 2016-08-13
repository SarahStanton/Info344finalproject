from django.db import models


# Create your models here.


class Category(models.Model):
	folder = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.folder


class Picture(models.Model):
	link = models.URLField(max_length=300, null=True)
	category = models.ForeignKey(Category, null=True)

	def __str__(self):
		return self.link