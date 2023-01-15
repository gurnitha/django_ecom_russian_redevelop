# app/product/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.product.models import Category


# ModelAdmin:CategoryAdmin
# Customizing Category table display in admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']

# Register models
admin.site.register(Category, CategoryAdmin)