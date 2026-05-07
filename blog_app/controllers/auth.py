from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .base import BaseController
from ..forms import LoginForm, RegisterForm


class LoginController(BaseController):
    _CLASS_FORM = LoginForm
    _PAGE_CONTEXT = {
        "form": {
            "title": "Вход",
            "page_title": "Вход",
            "additional_text": "Еще не с нами ?",
            "additional_link": "/register",
            "link_text": "Зарегистрируйтесь",
            "btn_text": "Войти"
        }
    }
    _FORM_REDIRECT_PAGE = "home"

    def _form_submit(self):
        username = self.form.cleaned_data["username"]
        password = self.form.cleaned_data["password"]

        user = authenticate(
            self._request,
            username=username,
            password=password
            )
        if user:
            login(self._request, user)
            return True

        return False

    def logout(self):
        logout(self._request)
        return redirect("login")

class RegisterController(BaseController):
    _CLASS_FORM = RegisterForm
    _PAGE_CONTEXT = {
        "form": {
            "title":"Регистрация",
            "page_title":"Регистрация в системе",
            "additional_text": "Уже зарегистрированы ?",
            "additional_link": "/login",
            "link_text":"Авторизуйтесь",
            "btn_text":"Зарегистрироваться"
        }
    }
    _FORM_REDIRECT_PAGE = "login"
