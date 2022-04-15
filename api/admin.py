from django.contrib import admin
from django.contrib import admin
from .models import Admin, city, major

# Register your models here.
@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ['id' , 'username', 'password']

@admin.register(city)
class city(admin.ModelAdmin):
    list_display = ['id' , 'name']

@admin.register(major)
class major(admin.ModelAdmin):
    list_display = ['id' , 'name']

