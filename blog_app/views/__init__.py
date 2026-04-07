from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html",
                  {
                    "title": "Главная",
                    "articles": None,
                    "popular_articles": None,
                  })