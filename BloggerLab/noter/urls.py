from django.urls import path
from . import views


app_name = "noter"

urlpatterns = [
    path('blogs/create', views.create_blog_view, name="create_blog_view"),
    path('details/<int:blog_id>', views.blog_details_view, name='blog_details_view')
]