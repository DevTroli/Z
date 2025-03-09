from django.urls import path
from .views import TweetListCreateView, TweetInteractionView

urlpatterns = [
    path("tweets/", TweetListCreateView.as_view(), name="tweet-list-create"),
    path(
        "tweets/<int:pk>/<str:action>/",
        TweetInteractionView.as_view(),
        name="tweet-interaction",
    ),
]
