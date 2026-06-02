from django.shortcuts import render
from .category import category_list, category_form, category_delete
from .auth import login_page, register_page, logout_page

# Create your views here.
def home(request):
    return render(request, "home.html",
                  {
                    "title": "Главная",
                    "articles": None,
                    "popular_articles": None,
                  })