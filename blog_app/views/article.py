from blog_app.controllers import ArticleController

def article_form(request, article_id: int | None = None):
    return ArticleController(request, article_id).form_page()

def article_delete(request, article_id: int):
    return ArticleController(request, article_id).delete()