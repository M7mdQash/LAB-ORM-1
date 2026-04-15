from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Blog

# Create your views here.

def create_blog_view(request:HttpRequest):
    if request.method == "POST":
        print(request.POST)
        new_blog = Blog(title=request.POST["title"],
                        content=request.POST["content"],
                        is_published=request.POST.get("is_published") == "on",
                        published_at=request.POST["published_at"],
                        )
        if request.FILES.get("image"):
            new_blog.image = request.FILES["image"]
        if request.FILES.get("file"):
            new_blog.files = request.FILES["file"]
        new_blog.save()
    return render(request, "noter/blog_creation.html")

def blog_details_view(request:HttpRequest,blog_id:int):
    blog = Blog.objects.get(pk=blog_id)
    print(blog)
    return render(request,'noter/blog_details.html',{"blog":blog})