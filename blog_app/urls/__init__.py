from django.urls import path
from blog_app import views
from .category import category_urls
from .auth import auth_urls
from .article import article_urls

urlpatterns = [
    path("", views.home, name="home"),
    *category_urls,
    *auth_urls,
    *article_urls,

]
