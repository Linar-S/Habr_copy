from django.shortcuts import render

from blog_app.controllers import CategoryController


def category_list(request):
    return render(request, "category/list.html", {
        "title": "Все категории",
        "popular_articles": None,
        "categories": None,
     }
    )

def category_add(request):
    return CategoryController(request).form_page()
