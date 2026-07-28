from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, SET_NULL, CASCADE

from .article import Article


class View(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True )
    article = ForeignKey(Article, on_delete=CASCADE)
