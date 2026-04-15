from django.shortcuts import redirect, render
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

def blog_update_view(request:HttpRequest,blog_id:int):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST.get("is_published") == "on"
        blog.published_at = request.POST["published_at"]
        if request.FILES.get("image"):
            blog.image = request.FILES["image"]
        if request.FILES.get("file"):
            blog.files = request.FILES["file"]
        blog.save()
        
        return redirect("noter:blog_details_view",blog_id=blog_id)
    return render(request,'noter/blog_update.html',{"blog":blog})


def blog_delete_view(request:HttpRequest,blog_id:int):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect("main:home_view")