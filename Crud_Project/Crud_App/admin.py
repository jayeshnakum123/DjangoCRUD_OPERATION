from django.contrib import admin
from .models import Student_info

# Register your models here.


@admin.register(Student_info)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password", "image")
