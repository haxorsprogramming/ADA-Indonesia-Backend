from django.contrib import admin

# Register your models here.
from .models import dataPost

class dlAdmin(admin.ModelAdmin):
    list_display = [
        'judul', 
        'slug', 
        'short_deks', 
        'long_deks',
        'cover_homepage', 
        'img_feature',
        'writer'
    ]
    list_per_page = 30

admin.site.register(dataPost, dlAdmin) 