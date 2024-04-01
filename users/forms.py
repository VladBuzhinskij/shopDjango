from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model=User
    # username = forms.CharField(
    #     label='Имя пользователя',
    #     widget=forms.TextInput(attrs={
    #         "autofocus":True,
    #         "class":"inpreg",
    #         "placeholder":"Введите имя пользователя" 
    #     }))
    # password=forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplite":"current_password",
    #         "class":"inpreg",
    #         "placeholder":"Введите пароль"
    #     })
    # )
    

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField()
    last_name= forms.CharField()
    email= forms.CharField()
    address= forms.CharField()
    class Meta:
        model=User
        fields=(
            "username",
            "first_name",
            "last_name",
            "address",
            "email",
            "password1",
            "password2",
        )

class ProfileForm(UserChangeForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name= forms.CharField()
    email= forms.CharField()
    address= forms.CharField()
    class Meta:
        model=User
        fields=(
            "username",
            "first_name",
            "last_name",
            "address",
            "email",
        )
    
    