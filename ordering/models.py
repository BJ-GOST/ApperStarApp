from django.db import models
from django.conf import settings


CATS = (
	('Web Development', 'Web Development'),
	('Information System Development', 'Information System Development'),
	('Mobile App Development', 'Mobile App Development'),
	('Graphics Design', 'Graphics Design')
	)

PURPOSES = (
	('Ecommerce', 'Ecommerce'),
	('Informative', 'Informative'),
	('Blog', 'Blog'),
	('Advertisement', 'Advertisement'),
	('Portfolio', 'Portfolio'),
	# if other please state the purpose
	('Other', 'Other') 
	)

SYS_TYPES = (
	('Management', 'Management'),
	('Financial', 'Financial'),
	('Inventory', 'Inventory')
)

BANNERS = (
	('Teardrop', 'Teardrop'),
	('Backdrop', 'Backdrop'),
	('Rollup', 'Rollup')
)

GRAPHIC_TYPE = (
	('Cards', 'Cards'),   
	('Banners', 'Banners'),
)



#this is a model for creating jobs; it has many fields that are used in the generation of multiple forms
class Job(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	category = models.CharField(max_length=255, choices=CATS)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	accepted = models.BooleanField(null=True, blank=True)
	scheduled = models.BooleanField(null=False, default=False)
	apper = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='apper')
	descriptive_purpose = models.TextField(null=True)


	#WebDev -- these are the options for a job in the webdev category
	title = models.CharField(max_length=255, blank=False, null=True)
	description = models.TextField(blank=True, null=True)
	purpose = models.CharField(blank=True, null=True, max_length=255, choices=PURPOSES)
	other = models.TextField(blank=True, null=True)
	features = models.TextField(blank=True, null=True)
	pages = models.IntegerField(blank=True, null=True)
	theme = models.CharField(blank=True, null=True, max_length=255)

	#Desktop Application
	sys_type = models.CharField(max_length=225, choices=SYS_TYPES, null=True)
	modules = models.TextField(null=True)
	
	#Graphic designer
	banner_type = models.CharField(max_length=255, choices=BANNERS, null=True)
	graphic_type = models.CharField(max_length=255, choices=GRAPHIC_TYPE, null=True)




#this is a model for creating notification each time a new job is created 
class Notification(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	category = models.CharField(max_length=255, choices=CATS, null=True, blank=True)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	body = models.TextField(blank=True, null=True)
	viewed = models.BooleanField(null=False, default=False)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)



#this is a model like the notification model named messages and used to display notifications on the clients side 
#dear future me and whoever will be refactoring this code in future; i don't know what you think but i actually thought it was a wise idea to create two different models (Notication and Message to handle something that was almost the same idea
class Message(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
	body = models.CharField(max_length=255, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	viewed = models.BooleanField(default=False, null=False)



#this is a model for scheduling the jobs
class Schedule(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	moduleName = models.CharField(max_length=255, blank=False, null=True)
	description = models.TextField(blank=False, null=True)
	completed = models.BooleanField(null=False, default=False)
	

