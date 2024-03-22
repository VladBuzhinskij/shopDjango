from django.contrib import admin
from products.models import Categories,SubCategories,Products
# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
