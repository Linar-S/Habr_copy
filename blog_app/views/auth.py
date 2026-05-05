from django.shortcuts import render, redirect
from blog_app.forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm()
    return render(request, "form.html",
                  {
                      "title": "Вход",
                      "page_title": "Вход",
                      "form": form,
                      "additional_text": "Еще не с нами ?",
                      "additional_link": "/register",
                      "link_text":"Зарегистрируйтесь",
                      "btn_text":"Войти"
                  }
                  )

def register_page(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "form.html", {
        "title":"Регистрация",
        "page_title":"Регистрация в системе",
        "form": form,
        "additional_text": "Уже зарегистрированы ?",
        "additional_link": "/login",
        "link_text":"Авторизуйтесь",
        "btn_text":"Зарегистрироваться"

    }
    )