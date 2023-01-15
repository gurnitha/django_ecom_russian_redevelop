# app/home/urls.py

# Import django modules
from django.urls import path

# Import from loclas
from app.home import views

# Add app name
app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]