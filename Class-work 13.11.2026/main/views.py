from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm
from .services.user_service import create_user
def home(request):
    return render(request, "main/home.html")
def register(request):
    if request.user.is_authenticated: return redirect("profile")
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = create_user(username=form.cleaned_data["username"], email=form.cleaned_data["email"], password=form.cleaned_data["password1"], avatar=form.cleaned_data.get("avatar"))
            login(request, user)
            messages.success(request, "Your account has been created successfully.")
            return redirect("profile")
    else: form = RegistrationForm()
    return render(request, "main/register.html", {"form":form})
class UserLoginView(LoginView):
    template_name = "main/login.html"
    authentication_form = LoginForm
class UserLogoutView(LogoutView): pass
@login_required
def profile(request):
    return render(request, "main/profile.html", {"profile_user":request.user})
