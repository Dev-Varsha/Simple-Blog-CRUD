from django.contrib import admin
from .models import (
    Tag,
    Blog,
)
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    """admin for Tag"""
    list_display = [
        'name',
    ]

class BlogAdmin(admin.ModelAdmin):
    """admin for Blog"""
    search_fields=['title']
    list_display = [
        'title',
        'content',
        'image',
        'tags',
    ]

admin.site.register(Tag)
admin.site.register(Blog)