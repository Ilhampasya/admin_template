from .models import *
from django.contrib import admin

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Post, PostModelAdmin)
