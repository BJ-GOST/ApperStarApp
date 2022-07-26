from django.contrib import admin
from .models import Job, Notification, Message, Schedule


admin.site.register(Job)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(Schedule)