from django.urls import path 
from . import views

urlpatterns = [
path('jobs/<str:pk>/', views.jobs_page, name='jobs'),
path('job-select', views.job_select, name='job-select'),
path('custom-job', views.custom_job, name='custom-job'),
path('guided-job', views.guided_job, name='guided-job'),
path('graphics-design', views.graphics, name='graphics-design'),
path('web-development', views.webdev, name='web-development'),
path('info-systems', views.info_systems, name='info-systems'),
path('app-development', views.appdev, name='app-development'),
path('job/<str:pk>', views.job_detail, name='job-detail'),
path('all-notifications', views.all_notifications, name='all-notifications'),
path('notification/<str:pk>/', views.notification_detail, name='notification-detail'),
path('accept', views.accept, name='accept'),
path('deny', views.deny, name='deny'),
path('accepted-jobs/<str:pk>/', views.accepted_jobs, name='accepted-jobs'),
path('my-notifications/<str:pk>/', views.my_notifications, name='my-notifications'),
path('schedule-job/<str:pk>/', views.job_scheduling, name='schedule-job'),
path('schedule', views.schedule, name='schedule'),
path('scheduled-jobs/<str:pk>/', views.scheduled_jobs, name='scheduled-jobs'),
path('scheduled-job/<str:pk>/', views.scheduled_job_detail, name='scheduled-job-detail'),
path('complete', views.complete, name='complete'),
path('viewed', views.viewed, name='viewed'),
path('search', views.search, name='search'),
path('pay', views.payment, name='pay'),#payment url
path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
path('payment', views.payment_form, name='payment'),
path('easy_pay', views.easy_pay, name='easy_pay')
]