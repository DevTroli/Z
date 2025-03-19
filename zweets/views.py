from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Zweet


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
