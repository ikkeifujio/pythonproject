from django.contrib import admin

from django.contrib import admin
from .models import Post, Comment, Account, Schedule
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(Schedule)