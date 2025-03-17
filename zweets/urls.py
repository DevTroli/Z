from django.urls import path
from .views import FeedView, ZweetCreateView

app_name = "zweets"

urlpatterns = [
    path("", FeedView.as_view(), name="feed"),
    path("create/", ZweetCreateView.as_view(), name="create"),
]
