from django.shortcuts import render

def category_list(request):
    return render(request, "category/list.html", {
        "title": "Все категории",
        "popular_articles": None,
        "categories": None,
     }
    )
