from django.contrib import admin

from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
