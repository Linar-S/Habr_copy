from django.shortcuts import render

from blog_app.controllers import ArticleController
from blog_app.models import Article


def article_form(request, article_id: int | None = None):
    return ArticleController(request, article_id).form_page()

def article_delete(request, article_id: int):
    return ArticleController(request, article_id).delete()


def article_view(request, article_id: int):
    return ArticleController(request, article_id).view()


def article_user(request, user_id: int):
    return ArticleController(request).list_by_user(user_id)


def article_category(request, category_id: int):
    return ArticleController(request).list_by_category(
        category_id
    )


def articles_list(request):
    return ArticleController(request).list()
