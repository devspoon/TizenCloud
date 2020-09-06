from django.contrib import admin
from .models import Authentication

# Register your models here.

class AuthAdmin(admin.ModelAdmin):
    list_display = ('id','email','image','result','register_date')

admin.site.register(Authentication, AuthAdmin)
