from .category import category_urls
from .auth import auth_urls
from .article import article_urls

urlpatterns = [
    *category_urls,
    *auth_urls,
    *article_urls
]
