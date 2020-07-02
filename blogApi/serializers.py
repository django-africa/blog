from rest_framework import serializers, fields
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Category


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class PostSerializer(serializers.ModelSerializer, TaggitSerializer):
    author = UserProfileSerializer()
    created_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'], required=False)
    published_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'], required=False)
    category = CategorySerializer()
    tags = TagListSerializerField()
    view_count = fields.IntegerField(source='get_count', required=False)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(required=False)

    class Meta:
        fields = "__all__"
        model = Comment


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PrayerRequest



