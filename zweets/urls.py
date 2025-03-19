from django.urls import path
from .views import FeedView, ZweetCreateView, ZweetDetailView, LikeZweetView, AddCommentView

app_name = "zweets"

urlpatterns = [
    path("", FeedView.as_view(), name="feed"),
    path("create/", ZweetCreateView.as_view(), name="create"),
    path("<int:pk>/", ZweetDetailView.as_view(), name="zweet_detail"),
    path("<int:pk>/like/", LikeZweetView.as_view(), name="like_zweet"),
    path("<int:pk>/comment/", AddCommentView.as_view(), name="add_comment"),
]
