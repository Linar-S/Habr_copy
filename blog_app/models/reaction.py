from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE, BooleanField
from .article import Article
from .comments import Comment

class Reaction(Model):
    is_like = BooleanField()
    user = ForeignKey(User, on_delete=CASCADE)
    article = ForeignKey(Article, on_delete=CASCADE, null=True)
    comment = ForeignKey(Comment, on_delete=CASCADE, null=True)