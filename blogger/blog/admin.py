from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)
class Pro(admin.StackedInline):
    model = Profile

class user_up(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [Pro]

admin.site.register(User,user_up)
# admin.site.register(Profile)