from django.contrib.auth.models import User
from django.shortcuts import render

from blog_app.forms import ArticleForm
from .base import BaseController
from blog_app.models import Article, Category, Comment, View


class  ArticleController(BaseController):
    _CLASS_FORM = ArticleForm
    _REDIRECT_PAGE = "home"
    _MODEL = Article
    _ENTITY_NAME = "статью"

    def list(self, models = None):
        return super().list_page(
            "article/list.html",
            "Главная",
            models
        )

    def list_by_user(self, user_id: int):
        user = User.objects.get(pk=user_id)
        models = []

        if user:
            models = Article.objects.filter(user=user) or []

        return self.list(models)

    def list_by_category(self, category_id: int):
        category = Category.objects.get(pk=category_id)
        models = []

        if category:
            models = Article.objects.filter(
                category=category
            ) or []

        return self.list(models)

    def view(self):
        article: Article = Article.objects.get(pk=self._entity_id)


        return render(
            self._request,
            "article/view.html",
            {
                "article": article,
                **self._get_extra_article_data(article)
            }
        )

    def _before_form_save(self, form: ArticleForm):
        form.instance.user = self._request.user

    def _has_access(self):
        return (self._request.user
                and self._entity_id
                and (entity := self._MODEL.objects.get(pk=self._entity_id))
                and self._request.user.id == entity.user.id
                )

    def _get_extra_article_data(self, article: Article) -> dict:
        comments: list[Comment] = Comment.objects.filter(article=article) or []
        views_count: int = len(View.objects.filter(article=article) or [])

        return {
            "comments": comments,
            "comments_count": len(comments),
            "views_count": views_count
        }
