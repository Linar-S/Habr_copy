from django.shortcuts import render
from blog_app.forms import LoginForm



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
                  }
                  )