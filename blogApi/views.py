from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer, PrayerRequestSerializer, \
    CategorySerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Category
from hitcount.views import HitCountDetailView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet, HitCountDetailView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    count_hit = True


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PrayerRequestViewSet(viewsets.ModelViewSet):
    serializer_class = PrayerRequestSerializer
    queryset = PrayerRequest.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



