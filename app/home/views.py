# app/home/views.py
from django.shortcuts import render


# VIEWS: index
def home_page(request):
    return render(request,'index.html')
