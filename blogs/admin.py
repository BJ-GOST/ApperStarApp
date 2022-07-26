from django.contrib import admin
from .models import *

admin.site.register(blog)
admin.site.register(comment)
admin.site.register(reply)
admin.site.register(like)
admin.site.register(subscription)

