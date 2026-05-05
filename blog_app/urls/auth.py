from django.urls import path

from blog_app.views import login_page
from blog_app.views import register_page

auth_urls = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register")
]

