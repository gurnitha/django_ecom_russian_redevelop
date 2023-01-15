# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.home.urls', namespace='home')),
    path('admin/', admin.site.urls),
]