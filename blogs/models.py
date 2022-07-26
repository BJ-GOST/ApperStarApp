from django.db import models

# Create your models here.

from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.

class blog(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', default=1)
	blog_pic = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	content = HTMLField(default='something')
	liked = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='likes')
	
	def __str__(self):
		return str(self.title)
	
	@property
	def num_likes(self):
		return self.liked.all().count()




class comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', null=True)
	body = models.CharField(max_length=500)
	blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='comments')
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.body)

	class Meta:
		ordering = ['timestamp']




class reply(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reply', null=True)
	body 	= models.CharField(max_length=500)
	comment = models.ForeignKey(comment, on_delete=models.CASCADE, related_name='replies')
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		ordering = ['timestamp']

	def __str__(self):
		return str(self.body)


LIKE_CHOICES = (

	('like', 'like'),
	('unlike', 'unlike')

)

class like(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	blog = models.ForeignKey(blog, on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

	def __str__(self):
		return str(self.blog)


class subscription(models.Model):
	blogger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	email = models.EmailField()

	def __str__(self):
		return str(self.blogger)



		