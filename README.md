# Инструкция по созданию и настройке окружения

### Шаг 1
Создать новый проект с uv

---

### Шаг 2
Установить ```Django``` и ```psycopg2```

```bash
    uv add django psycopg2
```

---

### Шаг 3
Создаем менеджер приложений:
```bash
    uv run django-admin startproject blog_manager .
```

---

### Шаг 4
Создаем приложение:
```bash
   uv run manage.py startapp blog_app
```

---

### Шаг 5
Регистрируем приложение в менеджере:
* В менеджере приложении (```blog_manager```) открыть файл ```settings.py```
* Найти переменную ```INSTALED_APPS```
* Добавить в нее первой строкой класс конфига приложения в формате: ```<Пакет>.<Модуль>.<Название класса>``` (```blog_app.apps.BlogAppConfig,```)

---

### Шаг 6
Запустить сервер:
```bash
    uv run manage.py runserver
```

---

### Шаг 7
* Создаем базу данных в pgAdmin
* В менеджере приложении (```blog_manager```) открыть файл ```settings.py```
* На переменной ```DATABASES``` перейти по ссылки и скопировать пример конфига для PostgreSQL
* Заменить конфиг в ```DATABASES``` и исправить под локальные данные

---

### Шаг 8
Применить базовые миграции Django:
```bash
    uv run manage.py migrate
```

---

### Шаг 9
Создание суперпользователя:
```bash
    uv run manage.py createsuperuser
```
и следовать его инструкциям

    | Во время ввода пороля и его повтора они не отображаются

---

### Шаг 10
Войти под пользователем из шага 9 на ```http://127.0.0.1:8000/admin/```

---

### Шаг 11
* В папке с приложением создать папку ```templates``` (```blog_app/templates```)
* В папке с приложением создаем папку ```static``` (```blog_app/static```)
* В папке ```templates``` создаем ```base.html``` и ```home.html``` (шаблон главной страницы расширающий base.html)
* В папке ```static``` создать папки ```css``` и ```js```, в них добавить ```index.css``` и ```index.js```

---

### Шаг 12
* Создать в папке приложения пакет ```views```. Добавить в ```__init__.py``` представление для главной страницы

```python
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
```

* Создать в папке приложения пакет ```urls```. Добавить в ```__init__.py``` маршрут до главной страницы

```python
from django.urls import path
from blog_app import views


urlpatterns = [
    path("", views.home, name="home"),
]
```

* Подключем ```blog_app/urls``` в blog_manager ```urls```

```python
from django.contrib import admin
from django.urls import path, include
from blog_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
```
---

### Шаг 13
* Реализовать базовый шаблон (```base.html``) и стили (```index.css```)
* Расширить базовый шаблон на главной странице (```home.html```)

home.html:
```html
{% extends "base.html" %}

{% block content %}
            <div> КОНТЕНТ </div>

{% endblock %}

```

base.html:
```html
{% load static %}
<!DOCTYPE html>
<html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Habr Copy</title>

</head>
<body>
    <nav>
        <div><a href="{% url 'home' %}"></a></div>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

---


