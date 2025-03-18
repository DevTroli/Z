from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from users.models import User


class ZLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get("next", "")
        return next_url or reverse_lazy("zweets:feed")


class ZSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "auth/signup.html"
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class ZLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "bio"]
    template_name = "users/edit_profile.html"
    success_url = reverse_lazy("zweets:feed")

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget.attrs.update({"class": "form-control"})
        form.fields["bio"].widget.attrs.update({"class": "form-control"})
        return form
