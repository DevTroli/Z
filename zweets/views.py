from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Zweet


class FeedView(ListView):
    model = Zweet
    template_name = "zweets/feed.html"
    context_object_name = "zweets"
    paginate_by = 10

    def get_queryset(self):
        return Zweet.objects.select_related("user").prefetch_related("likes")[
            :20
        ]  # Temporário para testes


class ZweetCreateView(CreateView):
    model = Zweet
    fields = ["content"]
    template_name = "zweets/feed.html"
    success_url = reverse_lazy("zweets:feed")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
