from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	SapID = models.IntegerField(default = 60000000000, unique = True)
	history = models.TextField(blank = True)

	def __str__(self):
		return self.user.username

class Book(models.Model):
	libID = models.CharField(max_length = 400, default = ' ')
	area = models.CharField(max_length = 400, default = ' ')
	subject = models.CharField(max_length = 400, default = ' ')
	bookName = models.CharField(max_length = 400)
	author = models.CharField(max_length = 200)
	publication = models.CharField(max_length = 200, default = ' ')
	copies = models.IntegerField(default = 1)
	issuedTo = models.TextField(blank = True)
	requestedBy = models.TextField(blank = True)
	requests  = models.IntegerField(default = 0)

	def __str__(self):
		return self.bookName 
						