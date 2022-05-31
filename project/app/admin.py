from django.contrib import admin

from django.contrib import admin
from .models import Post, Comment, Account, Schedule, Goal, IndividualSchedule, Role
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(Schedule)
admin.site.register(Goal)
admin.site.register(IndividualSchedule)
admin.site.register(Role)