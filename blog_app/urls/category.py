from django.urls import path
from blog_app import views


category_urls = [
    path("category/list/", views.category_list, name="category-list"),
]
