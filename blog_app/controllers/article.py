from blog_app.controllers.base import BaseController
from blog_app.forms import ArticleForm
from blog_app.models import Article


class ArticleController(BaseController):
    _CLASS_FORM = ArticleForm
    _REDIRECT_PAGE = "home"
    _ENTITY_NAME = "статью"

    _MODEL = Article

    def _before_form_save(self, form: ArticleForm):
        form.instance.user = self._request.user
