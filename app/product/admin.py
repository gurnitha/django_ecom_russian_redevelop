# app/product/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.product.models import Category, Product, Images


# ModelAdmin:CategoryAdmin
# Customizing Category table display in admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']


# Defining ProductImageInline class 
# to show more image fields in Product table
# when creating or udating a product
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

# ModelAdmin:ProductAdmin
# Customizing Product table display in admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status', 'image_tag'] # image_tag to show product image in admin panel
    list_filter = ['category']
    # readonly_fields is showing an image (just like an icon) in 
    # the field image of Product table, when to updating a product
    readonly_fields = ('image_tag',) 
    inlines = [ProductImageInline] # Apply the ProductImageInline class

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)

