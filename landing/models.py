from django.db import models

# Create your models here.

class Portfolio(models.Model):
	"""docstring for Portfolio"""
	project_name = models.CharField(max_length=200)
	client = models.CharField(max_length=100)
	website = models.URLField(max_length=200)
	service = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='portfolios',blank=True,null=True)
	added_date = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.project_name

	def __str__(self):
		return self.project_name


class Cms(models.Model):
	"""docstring for Cms"""
	headline = models.CharField(max_length=100)
	about_me = models.TextField()
	about_sub = models.TextField(blank=True, null=True, default = "")
	facebook = models.CharField(max_length=100,blank=True, null=True)
	twitter = models.CharField(max_length=100,blank=True, null=True)
	gplus = models.CharField(max_length=100,blank=True, null=True)
	linkedin = models.CharField(max_length=100,blank=True, null=True)

	def __str__(self):
		return self.headline

	def __unicode__(self):
		return self.headline


class Service(models.Model):
	"""Class to manage the services provided"""

	name = models.CharField(max_length=50)
	detail = models.TextField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Contact(models.Model):
	"""Messages left by customers"""

	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name
		
			
	
