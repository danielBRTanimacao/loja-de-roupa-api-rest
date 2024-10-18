from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = '-id',
    search_fields = ['id', 'name']
    list_per_page = 15
    list_max_show_all = 100

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'origin']
    list_display_links = ['id', 'name']
    ordering = '-id',
    search_fields = ['id', 'name', 'origin']
    list_per_page = 15
    list_max_show_all = 100

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value']
    list_display_links = ['id', 'name']
    ordering = '-id',
    search_fields = ['id', 'name']
    list_per_page = 15
    list_max_show_all = 100