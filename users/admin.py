from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.admin import UserAdmin 
# Register your models here.


admin.site.register(User,UserAdmin)

admin.site.unregister(Group)