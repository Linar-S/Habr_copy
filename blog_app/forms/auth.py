from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    label_name = {
        "username":"Имя пользователя",
        "email":"Электронная почта",
        "password1":"Пароль",
        "password2": "Повторите пароль",
    }

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.help_text = None
            field.label = self.label_name[filed_name]

