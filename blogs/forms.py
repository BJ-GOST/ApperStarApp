from django import forms 
from .models import *
from tinymce.widgets import TinyMCE
import tinymce
from django.forms import Select, Textarea, TextInput, NumberInput


class blogform(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 30}))
	class Meta:
		model 	= blog 
		fields 	= ['content', 'title', 'blog_pic' ]
		


class commentform(forms.ModelForm):
	class Meta:
		model 	= comment
		fields 	= ['body']
		widgets = {
		'body':Textarea(attrs={
				'placeholder':'please leave a comment',
				'style': 'width:100%; height:100px; color:white; background:transparent; text-align:center;'
			})
		}


class replyform(forms.ModelForm):
	class Meta:
		model 	= reply
		fields 	= ['body']
		widgets = {
		'body':Textarea(attrs={
				'placeholder':'Reply',
				'style': 'width:100%; height:100px; color:white; background:transparent; text-align:center;'
			})
		}


class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = subscription
		fields = ['email']



		