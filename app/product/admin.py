# app/product/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.product.models import Category, Product


# ModelAdmin:CategoryAdmin
# Customizing Category table display in admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']


# ModelAdmin:ProductAdmin
# Customizing Product table display in admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status']
    list_filter = ['category']

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

