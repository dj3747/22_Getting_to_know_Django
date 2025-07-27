from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from dotenv import load_dotenv

from .forms import CustomAuthenticationForm, CustomUserCreationForm

load_dotenv()


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:home")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                "Добро пожаловать!",
                "Вы успешно зарегистрировались в магазине.",
                "EMAIL_HOST_USER",
                [user.email],
                fail_silently=False,  # Для отладки - покажет исключение при ошибке
            )
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")
