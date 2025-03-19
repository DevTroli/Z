from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView, DetailView, View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from users.models import User, Follow
from zweets.models import Zweet


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


class ProfileView(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_zweets = Zweet.objects.filter(user=self.object)

        context["zweets"] = user_zweets[:20]
        context["total_zweets"] = user_zweets.count()

        if self.request.user.is_authenticated:
            context["is_following"] = Follow.objects.filter(
                follower=self.request.user, followed=self.object
            ).exists()
        else:
            context["is_following"] = False

        return context


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


class FollowView(View):
    def post(self, request, username):
        followed = get_object_or_404(User, username=username)
        if request.user != followed:
            Follow.objects.get_or_create(follower=request.user, followed=followed)
        return redirect("profile", username=username)
