from django.urls import path

from blog_app.views import login_page

auth_urls = [
    path("login/", login_page, name="login")
]

