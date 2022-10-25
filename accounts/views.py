from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignUpForm


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_conformation = form.cleaned_data["password_conformation"]

        if password == password_conformation:
            user = User.objects.create_user(
                username,
                password=password,
            )
            user.save()

            login(request, user)

            return redirect("home")
        else:
            form.add_error("the passwords do not match")

    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
