# app/product/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.product.models import Category

# Register models
admin.site.register(Category)
