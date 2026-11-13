from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "avatar", "password1", "password2")
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
