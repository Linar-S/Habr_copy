from django.shortcuts import render
from .category import category_list
from .auth import login_page
from .auth import register_page

# Create your views here.
def home(request):
    return render(request, "home.html",
                  {
                    "title": "Главная",
                    "articles": None,
                    "popular_articles": None,
                  })