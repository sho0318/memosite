from django.contrib import admin
from .models import CustomUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'email']

admin.site.register(CustomUser, UserAdmin)