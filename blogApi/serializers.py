from rest_framework import serializers, fields
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Category
  

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'password')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class PostSerializer(serializers.ModelSerializer, TaggitSerializer):
    created_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'], required=False)
    published_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'], required=False)
    category = CategorySerializer(required=False)
    view_count = fields.IntegerField(source='get_count', required=False)

    class Meta:
        fields = "__all__"
        model = Post
        ordering = ['-id']


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(required=False)

    class Meta:
        fields = "__all__"
        model = Comment


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PrayerRequest
