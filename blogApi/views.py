from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer, AdvertSearlizer, PrayerRequestSerializer, CategorySerializer, ContactSearlizer
from .models import Post, Comment, UserProfile, PrayerRequest, Category, Contact, Advert
from hitcount.views import HitCountDetailView

User = get_user_model()
# Create your views here.
class PostViewSet(viewsets.ModelViewSet, HitCountDetailView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



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

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSearlizer
    queryset = Category.objects.all()

class AdvertViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertSearlizer
    queryset = Advert.objects.all()