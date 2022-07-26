from django.urls import path
from . import views

urlpatterns = [
path('createblog', views.createblog, name='createblog'),
path('', views.blogs, name='blogs'),
path('blog/<str:pk>/', views.blogdetail, name = 'blogdetail'),
path('comment/<str:pk>/', views.comment_detail, name='comment_detail'),
path('like', views.like_blog, name='like-blog'),
path('blog/<str:pk>/change', views.update_blog, name='update-blog'),
path('author/<str:pk>/', views.my_blogs, name='my-blogs'),
path('subscribers/<str:pk>', views.my_blogs, name='subscribers')
]

