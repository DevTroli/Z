from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Zweet, Comment


class FeedView(LoginRequiredMixin, ListView):
    model = Zweet
    template_name = "zweets/feed.html"
    context_object_name = "zweets"
    paginate_by = 10

    def get_queryset(self):
        return Zweet.objects.select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def Get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context["page_obj"]
        context["paginator_range"] = page_obj.paginator.get_elided_page_range(
            page_obj.number, on_each_side=1
        )
        return context


class ZweetCreateView(CreateView):
    model = Zweet
    fields = ["content"]
    template_name = "zweets/feed.html"
    success_url = reverse_lazy("zweets:feed")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ZweetDetailView(DetailView):
    model = Zweet
    template_name = "zweets/zweet_detail.html"
    context_object_name = "zweet"


class LikeZweetView(LoginRequiredMixin, View):
    def post(self, request, pk):
        zweet = get_object_or_404(Zweet, pk=pk)

        # Toggle like
        if request.user in zweet.likes.all():
            zweet.likes.remove(request.user)
        else:
            zweet.likes.add(request.user)

        # Redirect back to the referring page
        referer = request.META.get("HTTP_REFERER")
        if referer:
            return HttpResponseRedirect(referer)
        else:
            return HttpResponseRedirect(
                reverse("zweets:zweet_detail", kwargs={"pk": pk})
            )


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        zweet = get_object_or_404(Zweet, pk=pk)
        content = request.POST.get("content")

        if content:
            # Create new comment
            Comment.objects.create(user=request.user, zweet=zweet, content=content)
        else:
            messages.error(request, "O comentário não pode estar vazio.")

        return HttpResponseRedirect(reverse("zweets:zweet_detail", kwargs={"pk": pk}))
