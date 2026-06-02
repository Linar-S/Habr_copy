from blog_app.controllers.base import BaseController
from blog_app.forms import CategoryForm
from blog_app.models import Category


class CategoryController(BaseController):
    _CLASS_FORM = CategoryForm
    _REDIRECT_PAGE = "category-list"
    _ENTITY_NAME = "категорию"
    _ADDITIONAL_JS = ["categoryCard"]
    _MODEL = Category

