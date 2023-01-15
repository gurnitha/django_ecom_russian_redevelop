## DJANGO ECOMMERCE RUSSIAN REDEVELOP

Links:
Github 1: https://github.com/ingafter60/DJANGO-ECOM-RUSSIAN
Github redevelop: https://github.com/gurnitha/django_ecom_russian_redevelop
Github source: https://github.com/celikyuksell/Django-E-Commerce
Mysql: http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/


## Video 01. - Installation and setup


#### 01.1 Modified .gitignore and readme files
        
        Activities:

        1. modified:   .gitignore
        2. modified:   README.md

        NOTE: Initial commit done in Github


#### 01.2 Creating django project 'config'

        Activities:

        F:\_workspace\2023\ecom\django_ecom_russian_redevelop (main)
        1. λ python -m venv venv3931
           Create virtual environment 'venv3931'
        2. λ venv3931\Scripts\activate.bat
           Activate the venv3931
        3. (venv3931) λ pip install django==3.1.*
           Install django version 3.1
        4. (venv3931) λ python.exe -m pip install --upgrade pip
           Upgrade pip
        4. (venv3931) λ pip freeze
           Checking django version installed
        6. (venv3931) λ django-admin startproject config .
           Create django project 'config' in the root directory

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 01.3 Create django app 'app/home' 

        Activities:

        1. (venv3931) λ mkdir app\home
           Create directories
        2. (venv3931) λ django-admin startapp home app\home
           Create django app named 'home' in app directory

        modified:   README.md
        new file:   app/home/__init__.py
        new file:   app/home/admin.py
        new file:   app/home/apps.py
        new file:   app/home/migrations/__init__.py
        new file:   app/home/models.py
        new file:   app/home/tests.py
        new file:   app/home/views.py


#### 01.4 Register django home to config

        Activities:

        1. modified:   README.md
        2. modified:   app/home/apps.py
           Rename the app: 
           from name = 'home' to name = 'app.home'
        3. modified:   config/settings.py
           Register the app in INSTALLED_APPS:  
           'app.home.apps.HomeConfig',
        4. Testing run the server
           (venv3931) λ python manage.py runserver



## Video 02. - Templeting


#### 02.1 Adding and loading html templates


        1. Add static files
        new file:   app/home/static/css/bootstrap.min.css
        ...
        new file:   app/home/static/js/slick.min.js
        
        2. Craete homepage 
        new file:   app/home/templates/content.html
        new file:   app/home/templates/footer.html
        new file:   app/home/templates/header.html
        new file:   app/home/templates/homebase.html
        new file:   app/home/templates/index.html
        new file:   app/home/templates/sidebar.html
        new file:   app/home/templates/slider.html
        
        3. Create urls 
        new file:   app/home/urls.py
        # app/home/urls.py

           # Import django modules
           from django.urls import path

           # Import from loclas
           from app.home import views

           # Add app name
           app_name = 'home'

           urlpatterns = [
           path('', views.index, name='index'),
           ]

        4. Defining home_page view method
        modified:   app/home/views.py

           from django.shortcuts import render


           # VIEWS: index
           def home_page(request):
           return render(request,'index.html')
        
        5. Include or register home/urls.py 
        modified:   config/urls.py



## Video 03. - Creating Product App and Model


#### 03.1 Create a new app 'product'

        Activities:

        1. Create folder 
        (venv3931) λ mkdir app\product

        2. Create product app
        (venv3931) λ django-admin startapp product app\product

        modified:   README.md
        new file:   app/product/__init__.py
        new file:   app/product/admin.py
        new file:   app/product/apps.py
        new file:   app/product/migrations/__init__.py
        new file:   app/product/models.py
        new file:   app/product/tests.py
        new file:   app/product/views.py


#### 03.2 Register product app to config

        Aktivities:

        1. Mofified it
        modified:   README.md

        2. Rename the name of the app
        modified:   app/product/apps.py

        3. Register the app
        modified:   config/settings.py


#### 03.3 Create MySQL database 

        Aktivities:

        1. Modified
        modified:   README.md

        2. Create db
        mysql - u root -p
        mysql> create database django_ecom_russian_redevelop;

        3. Connect the db with the project
        modified:   config/settings.py
        DATABASES = {
         'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'django_ecom_russian_redevelop',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': 'localhost',
         }
        }

        4. Run and apply migrations
        (venv3931) λ python manage.py makemigrations
        (venv3931) λ python manage.py migrate


#### 03.4 Creating Category model for product

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Create Category model
        modified:   app/product/models.py
        # MODEL: Category
        class Category(models.Model):
         STATUS = (
         ('True', 'True'),
         ('False', 'False'),
         )
         parent      = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
         title       = models.CharField(max_length=30)
         keywords    = models.CharField(max_length=255)
         description = models.CharField(max_length=255)
         image       = models.ImageField(blank=True,upload_to='images/')
         status      = models.CharField(max_length=10, choices=STATUS)
         slug        = models.SlugField()
         create_at   = models.DateTimeField(auto_now_add=True)
         update_at   = models.DateTimeField(auto_now=True)

         class Meta:
         verbose_name_plural = 'Categories'

         def __str__(self):
         return self.title

        3. Run and apply migrations 
        new file:   app/product/migrations/0001_initial.py

        4. Register Category model
        modified:   app/product/admin.py


#### 03.5. Setting up media files

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Impor os and setup media url and root    
        modified:   config/settings.py
        import os
        MEDIA_URL = '/uploads/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

        3. Define path for media root and media url
        modified:   config/urls.py
        # config/urls.py
         from django.conf import settings
         from django.conf.urls.static import static
         from django.contrib import admin
         from django.urls import path, include

         urlpatterns = [
         path('', include('app.home.urls', namespace='home')),
         path('admin/', admin.site.urls),
         ]

         if settings.DEBUG: # new
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#### 03.6 From admin panel create parent category + image, child category + image 

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Creaete parent category
        new file:   uploads/images/chips.jpg

        3. Create child category
        new file:   uploads/images/desktop.jpg


#### 03.7 Create CategoryAdmin model to customizing Category table display in admin panel

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Customizing the admin panel
        modified:   app/product/admin.py
        # ModelAdmin:CategoryAdmin
         # Customizing Category table display in admin panel
         class CategoryAdmin(admin.ModelAdmin):
             list_display = ['title','parent', 'status']
             list_filter = ['status']

         # Register models
         admin.site.register(Category, CategoryAdmin)


#### 03.8 Create Product model

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Create Product model
        modified:   app/product/models.py
        class Product(models.Model):
          STATUS = (
              ('True', 'True'),
              ('False', 'False'),
          )
          title      = models.CharField(max_length=150)
          keywords   = models.CharField(max_length=255)
          description = models.CharField(max_length=255)
          image      = models.ImageField(blank=True,upload_to='images/product/')
          price      = models.FloatField()
          amount     = models.IntegerField()
          minamount  = models.IntegerField()
          detail     = models.TextField()
          slug       = models.SlugField()
          status     = models.CharField(max_length=10,choices=STATUS)
          create_at  = models.DateTimeField(auto_now_add=True)
          update_at  = models.DateTimeField(auto_now=True)

          def __str__(self):
              return self.title

        3. Run and apply migrations
        new file:   app/product/migrations/0002_product_alter_category_options_alter_category_image.py

        4. Register Product model to admin
        modified:   app/product/admin.py

        5. Renamed upload files in Category
        renamed:    uploads/images/chips.jpg -> uploads/images/category/chips.jpg
        renamed:    uploads/images/desktop.jpg -> uploads/images/category/desktop.jpg


#### 03.9 Add OneToMany relationship between Category model and Product model

        Aktivities:

        1. Modifies
        modified:   README.md
        
        2. Add OneToMany relationship Category and Product model
        modified:   app/product/models.py       

        3. Run and apply migrations 
        new file:   app/product/migrations/0003_product_category.py


#### 03.10 Add some items to products

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Add product belongs to parent category
        new file:   uploads/images/product/elecktronics.png

        3. Add product belongs to category
        new file:   uploads/images/product/hp_laptop.jpg


#### 03.11 Install django-ckeditor for product descrition field

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Install ckeditor
        (venv3931) λ pip install django-ckeditor

        3. Install pillow for images
        (venv3931) λ pip install pillow

        4. Configure ckeditor in settings.py
        modified:   config/settings.py

        4.1 Register ckeditor in INSTALLED_APPS
        'ckeditor',

        4.2 Configure ckeditor

         ####################################
         ##  CKEDITOR CONFIGURATION ##
         ####################################

         SITE_ID = 1

         CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

         CKEDITOR_UPLOAD_PATH = 'images/'
         CKEDITOR_IMAGE_BACKEND = "pillow"

         CKEDITOR_CONFIGS = {
             'default': {
                 'toolbar': None,
             },
         }

         ###################################

        5. Configur ckeditor path
        modified:   config/urls.py 

        6. Import and dse ckeditor in Product model       
        modified:   app/product/models.py
        from ckeditor_uploader.fields import RichTextUploadingField
        detail      = RichTextUploadingField()

        7. Testing add some text and image in detail
           field of the Product table 
           Result: Path of ckeditor: year/month/date
        new file:   uploads/images/2023/01/15/acer_c27.jpg
        new file:   uploads/images/2023/01/15/acer_c27_thumb.jpg


#### 03.12 Create ProductAdmin model to customizing Product table display in admin panel

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Customizing admin
        modified:   app/product/admin.py

         # ModelAdmin:ProductAdmin
         # Customizing Product table display in admin panel
         class ProductAdmin(admin.ModelAdmin):
             list_display = ['title','category', 'status']
             list_filter = ['category']


#### 03.13 Create Images model with OneTOMany relationship with Product model

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Create Images Model
        modified:   app/product/models.py

        class Images(models.Model):
          product = models.ForeignKey(Product,on_delete=models.CASCADE)
          title   = models.CharField(max_length=50,blank=True)
          image   = models.ImageField(blank=True, upload_to='images/product/')

          class Meta:
              verbose_name_plural = 'Images'

          def __str__(self):
              return self.title

        3. Run and apply migrations
        new file:   app/product/migrations/0004_alter_product_detail_images.py

        4. Register Images model to admin
        modified:   app/product/admin.py

        5. Testing:
        5.1 Added some products to Product table
        5.2 Added some images to Images table


#### 03.14 Using mark_safe to show image

        Aktivities:

        1. Modifies
        modified:   README.md

        2. Add mark_safe to Product table
        modified:   app/product/models.py

        # Showing product image in admin panel
        def image_tag(self):
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

        image_tag.short_description = 'Image'

        3. Add image_tag method in ProductAdmin model admin
        modified:   app/product/admin.py

        list_display = ['title','category', 'status', 'image_tag'] # image_tag to show product image in admin panel

        # readonly_fields is showing an image (just like an icon) in 
        # the field image of Product table, when to updating a product
        readonly_fields = ('image_tag',)

        NOTE: At last it works, after almost a full day debuging this error 

