from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
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
    """
    Create User

    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PrayerRequestViewSet(viewsets.ModelViewSet):
    serializer_class = PrayerRequestSerializer
    queryset = PrayerRequest.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class Registration(APIView):
