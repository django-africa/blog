from rest_framework import serializers, fields
from .models import Post, Comment, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()
    created_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'])
    published_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'])

    class Meta:
        fields = ('author', 'title', 'text', 'featured_image', 'created_date', 'published_date', 'summary')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    created_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'])
    email = fields.EmailField(source='get_email')
    user = UserProfileSerializer(required=False)
    profile_image = fields.FileField(source='get_profile_image')

    class Meta:
        fields = ('user', 'email', 'body', 'created_date', 'active', 'profile_image')
        model = Comment
