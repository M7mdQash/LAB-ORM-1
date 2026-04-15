from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db import models
from noter.models import Blog

# Create your views here.
def home_view(request:HttpRequest):
    blogs = Blog.objects.all()
    return render(request, 'main/home.html', {"Blogs":blogs})

# def create_blog_view(request:HttpRequest):
#     if request.method == "POST":
#         print(request.POST)
#         new_blog = Blog(title=request.POST["title"], content=request.POST["content"])
#         new_blog.save()
#     return render(request, "main/blog_creation.html")