from django.db import models


# Create your models here.
class Picture(models.Model):
	link = models.URLField(max_length=300, null=True)

	def __str__(self):
		return self.link