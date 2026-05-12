from django.forms import Textarea
from django.forms.fields import CharField

from blog_app.forms.base import BaseForm
from blog_app.models import Category


class CategoryForm(BaseForm):
    _LABEL_NAME = {
        "name":"Название",
        "icon":"Класс иконки FA",
        "description":"Описание"
    }

    name = CharField(required=True)
    icon = CharField(required=True)
    description = CharField(required=True, widget=Textarea)

    class Meta:
        model = Category
        fields = ["name", "icon", "description"]

