from django import forms
from django.forms import Select, Textarea, TextInput, NumberInput
from .models import * 



#this is a form for users who wish to describe their apps in a customised manner
class CustomJobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'category', 'description']
		widgets = {
			'category':Select(attrs={
				'style': 'width:100%; height:50px; color:white; background:rgb(0,0,20); border: 0px; border-bottom:1px solid white; font-size:large'
			}),
			'description':Textarea(attrs={
				'placeholder':'describe what you wish your app to be like',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent;'
			}),
			'title':TextInput(attrs={
				'placeholder': 'a title helps us identify your job',
				'style': 'width:100%; height:10vh; color:white; background:transparent; '
			}),
			}
 


#this will be changed to the form for the Web Development category
class WebDevForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'purpose', 'other', 'description', 'features', 'pages', 'theme']
		widgets = {
			'purpose':Select(attrs={
				'placeholder':'what do you intend to use the application for',
				'style': 'width:100%; height:50px; color:white; background:rgb(0,0,20); border: 0px; border-bottom:1px solid white; font-size:large'
			}),
            'description':Textarea(attrs={
            	'placeholder':'describe what you wish your app to be like',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent; font-size:12.5px;'
			}),
			'title':TextInput(attrs={
				'placeholder': 'a title helps us identify your job',
				'style': 'width:100%; height:10vh; color:white; background:transparent; font-size:12.5px;'
			}),
			'other':Textarea(attrs={
				'placeholder':'if purpose above is other please describe',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent; font-size:12.5px;'
			}),
			'features':Textarea(attrs={
				'placeholder':'what features would you like on your application',
				'style': 'width:100%; color:white; background:transparent; font-size:12.5px;'
			}),
			'theme':TextInput(attrs={
				'placeholder':'white, red, blue...',
				'style': 'width:100%; height:10vh; color:white; background:transparent; font-size:12.5px;'
			}),
			'pages':NumberInput(attrs={
				'placeholder':'How many pages would you like your web application or page to have',
				'style': 'width:100%; height:10vh; color:white; background:transparent; font-size:12.5px;'
			}),
		}


#remember to later on create on customised forms for each of the services offered

#a form for the graphics design category
class GraphicsDesignForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = [ 'title', 'banner_type', 'description', 'theme']
		widgets = {
			'description':Textarea(attrs={
				'placeholder':'describe what you wish your design to be like',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent;'
			}),
			'title':TextInput(attrs={
				'placeholder': 'a title helps us identify your job',
				'style': 'width:100%; height:10vh; color:white; background:transparent; '
			})
			}


#form for the Information Systems Category
class InformationSystemsDesign(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'description', 'sys_type', 'features']
		widgets = {
			'sys_type':Select(attrs={
				'style': 'width:100%; height:50px; color:white; background:rgb(0,0,20); border: 0px; border-bottom:1px solid white; font-size:large'
			}),
			'description':Textarea(attrs={
				'placeholder':'describe what you wish your app to be like',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent;'
			}),
			'title':TextInput(attrs={
				'placeholder': 'a title helps us identify your job',
				'style': 'width:100%; height:10vh; color:white; background:transparent; '
			}),
			'features':Textarea(attrs={
				'placeholder':'These are the features you would like the system to have; payment, registration',
				'style': 'width:100%; min-height:50vh; color:white; background:transparent;'
			}),
			}



#form for the Mobile App Development category
class MobileAppDev(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'description', 'descriptive_purpose', 'features']
		widgets = {
		'title':TextInput(attrs={
			'placeholder':'A title helps us identify your job',
			'style':'width:80%; height:10vh; background:transparent; color:linen'
			}),
		'description':Textarea(attrs={
			'placeholder':'Describe the app in as much detail as possible',
			'style':'width:80%; background:transparent; color:linen; margin-top:10px;'
			}),
		'descriptive_purpose':Textarea(attrs={
			'placeholder':'Describe the purpose of your app',
			'style':'width:80%; background:transparent; color:linen; margin-top:10px;'
			}),
		'features':Textarea(attrs={
			'placeholder':'What features would you like on your application?',
			'style':'width:80%; background:transparent; color:linen; margin-top:10px;'
			})
		}



#form for scheduling
class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule 
		fields = ['moduleName', 'description']
		widgets = {
		'moduleName':TextInput(attrs={
			'placeholder':'Enter the module name',
			'style':'width:80%; height:10vh; background:transparent; color:linen'
			}),
		'description':Textarea(attrs={
			'placeholder':'describe the module',
			'style':'width:80%; background:transparent; color:linen; margin-top:10px;'
			})
		}
