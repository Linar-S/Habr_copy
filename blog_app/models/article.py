from django.contrib.auth.models import User
from django.db.models import Model, TextField, CharField, ForeignKey, CASCADE

from .category import Category


class Article(Model):
    title = CharField(max_length=100)
    content = TextField()
    image = CharField(max_length=100)
    category = ForeignKey(Category, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title