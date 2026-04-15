from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Blog

# Create your views here.

def create_blog_view(request:HttpRequest):
    if request.method == "POST":
        print(request.POST)
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"])
        new_blog.save()
    return render(request, "noter/blog_creation.html")