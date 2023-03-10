# app/product/models.py

# Import django modules
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

# MODEL: Category
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent 		= models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title 		= models.CharField(max_length=30)
    keywords 	= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image 		= models.ImageField(blank=True,upload_to='images/category/')
    status 		= models.CharField(max_length=10, choices=STATUS)
    slug 		= models.SlugField()
    create_at 	= models.DateTimeField(auto_now_add=True)
    update_at 	= models.DateTimeField(auto_now=True)

    class Meta:
    	verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category 	= models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title 		= models.CharField(max_length=150)
    keywords 	= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image 		= models.ImageField(blank=True,upload_to='images/product/')
    price 		= models.FloatField()
    amount 		= models.IntegerField()
    minamount 	= models.IntegerField()
    detail      = RichTextUploadingField()
    slug 		= models.SlugField()
    status 		= models.CharField(max_length=10,choices=STATUS)
    create_at 	= models.DateTimeField(auto_now_add=True)
    update_at 	= models.DateTimeField(auto_now=True)

    # Showing product image in admin panel
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/product/')

    class Meta:
        verbose_name_plural = 'Images'
    def __str__(self):
        return self.title