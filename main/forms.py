from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class SignupForm(UserCreationForm):

    username = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Имя пользователя', 'class': 'form-control'}))

    email = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Эл. почта', 'class': 'form-control'}))

    password1 = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Пароль', 'class': 'form-control', 'type': 'password'}))

    password2 = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Подтверждение пароля', 'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')