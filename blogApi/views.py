from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer, PrayerRequestSerializer, CategorySerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Category
from hitcount.views import HitCountDetailView

User = get_user_model()
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

class Registration(FormView):
    form_class = UserCreationForm
    template_name = "blogApi/registration.html"
    success_url = "/"

    
    # def post( self, request):
    #     user = User.object.create(
    #         username=request.data.get('username'),
    #         email=request.data.get('email'),
    #     )
    #     user.set_password(str(request.data.get('password')))
    #     user.save()

    #     return Response({"status": "sucess", "response":"User Sucessfully Created"}, status.status.HTTP_201_CREATED)