from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer
from .models import Post, Comment, UserProfile
from hitcount.views import HitCountDetailView


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

