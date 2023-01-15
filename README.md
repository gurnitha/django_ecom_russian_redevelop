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