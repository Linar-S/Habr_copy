from django.shortcuts import render
from .category import category_list, category_form, category_delete
from .auth import login_page, register_page, logout_page
from .article import *
from ..models import Article


# Create your views here.
def home(request):
    return render(request, "home.html",
                  {
                    "title": "Главная",
                    "articles": Article.objects.all(),
                    "popular_articles": None,
                  })