from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, viewsets
from .serializers import PostSerializer, EventSerializer, CommentSerializer, UserProfileSerializer, AdvertSearlizer, PrayerRequestSerializer, CategorySerializer, ContactSearlizer, PublicationSerializer, MininstrySerializer
from .models import Post, Comment, UserProfile, Event, PrayerRequest, Category, Contact, Advert, Publication, Ministry
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
    queryset = Contact.objects.all()

class AdvertViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertSearlizer
    queryset = Advert.objects.all()

class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

class MinistriesViewset(viewsets.ModelViewSet):
    serializer_class = MininstrySerializer
    queryset = Ministry.objects.all()

class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()