from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'discount']
    list_filter = ['available']
    list_editable = ['price',  'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}
