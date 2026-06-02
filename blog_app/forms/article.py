from django.contrib.auth.models import User

from blog_app.forms.base import BaseForm
from blog_app.models.article import Article


class ArticleForm(BaseForm):
    _LABEL_NAME = {
        "title":"Заголовок",
        "content":"Статья",
        "image":"Ссылка на изображение",
        "category": "Категория статьи",

    }


    class Meta:
        model = Article
        fields = ["title",
        "content",
        "image",
        "category"]

