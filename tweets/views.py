# tweets/views.py
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer


def feed(request):
    return render(request, "feed.html")


# API View para listar e criar tweets
class TweetListCreateView(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.filter(parent_tweet__isnull=True).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# API View para interações (like, retweet)
class TweetInteractionView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, action):
        tweet = generics.get_object_or_404(Tweet, pk=pk)

        if action == "like":
            tweet.likes.add(request.user)
        elif action == "unlike":
            tweet.likes.remove(request.user)
        elif action == "retweet":
            tweet.retweets.add(request.user)

        return Response(TweetSerializer(tweet).data, status=status.HTTP_200_OK)


class TweetLikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        tweet = generics.get_object_or_404(Tweet, pk=pk)
        if request.user in tweet.likes.all():
            tweet.likes.remove(request.user)  # Descurtir
        else:
            tweet.likes.add(request.user)  # Curtir
        return Response(TweetSerializer(tweet).data, status=status.HTTP_200_OK)


class TweetRetweetView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        tweet = generics.get_object_or_404(Tweet, pk=pk)
        if request.user in tweet.retweets.all():
            tweet.retweets.remove(request.user)  # Desfazer retweet
        else:
            tweet.retweets.add(request.user)  # Retweetar
        return Response(TweetSerializer(tweet).data, status=status.HTTP_200_OK)


class TweetReplyView(generics.CreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        parent_tweet = generics.get_object_or_404(Tweet, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, parent_tweet=parent_tweet)
