from django.contrib import admin
from django.urls import path, include
from . import views
app_name='main'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    # path('blogs/create', views.create_blog_view, name="create_blog_view")
    # path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),

]