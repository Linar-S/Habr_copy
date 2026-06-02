from django.urls import path
from blog_app import views


article_urls = [
    path("article/add/", views.article_form, name="article-add"),
    path("article/update/<int:article_id>/", views.article_form, name="article-update"),
    path("article/delete/<int:article_id>/", views.article_delete, name="article-delete"),


]
