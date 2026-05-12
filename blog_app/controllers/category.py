from blog_app.controllers.base import BaseController
from blog_app.forms import CategoryForm


class CategoryController(BaseController):
    _CLASS_FORM = CategoryForm
    _FORM_REDIRECT_PAGE = "category-list"
    _PAGE_CONTEXT = {
        "form":{
            "title": "Добавить категорию",
            "page_title": "Добавить категорию",
            "btn_text": "Создать"
        }

    }