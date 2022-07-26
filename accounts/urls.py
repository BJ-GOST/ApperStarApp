from django.urls import path
from . import views 

urlpatterns = [
path('landing', views.landing, name='landing'),
path('apper', views.apper, name='apper'),
path('register', views.register, name= 'register'),
path('waiting', views.waiting, name='waiting'),
path('updateprofile', views.UpdateProfile, name= 'update-profile'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('password_reset', views.password_reset_request, name='password_reset')
]