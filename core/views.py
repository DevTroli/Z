from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Conta criada com sucesso para {username}!")
            return redirect("feed")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(
            f"Tentativa de login: username={username}, password={password}"
        )  # Log de depuração

        user = authenticate(request, username=username, password=password)
        print(f"Usuário autenticado: {user}")  # Log de depuração

        if user is not None:
            login(request, user)
            print(f"Usuário logado: {user.username}")  # Log de depuração
            return redirect("feed")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, "registration/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
