from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User 
from django.forms import Textarea, TextInput, EmailInput


class CreateProfile(UserCreationForm):
	class Meta:
		model = User 
		fields = ['salesName', 'username', 'email']
		widgets={
		'salesName':TextInput(attrs={
			'style': 'height:45px; width:250px'
			}),
		'username':TextInput(attrs={
			'style': 'height:45px; width:250px'
			}),
		'email':EmailInput(attrs={
			'style': 'height:45px; width:250px'
			})
		}


class UpdateProfile(UserChangeForm):
	class Meta:
		model = User
		fields = '__all__'