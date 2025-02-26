from rest_framework import serializers, fields
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Comment, UserProfile, Event, PrayerRequest, Advert, Category, Contact, Publication, Ministry
from drf_extra_fields.fields import Base64ImageField


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
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class PostSerializer(serializers.ModelSerializer, TaggitSerializer):
    class Meta:
        fields = "__all__"
        model = Post

    # def save(self, **kwargs):
    #     self.featured_image = base64_file(self.featured_image)
        
    #     return super(PostSerializer, self).save(**kwargs)

class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(required=False)

    class Meta:
        fields = "__all__"
        model = Comment


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PrayerRequest

class ContactSearlizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contact

class AdvertSearlizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Advert

    # def save(self, **kwargs):
    #     self.photo = Advert.objects.create(base64_file(self.photo))
        
    #     return super(AdvertSerializer, self).save(**kwargs)

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Publication

class MininstrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ministry

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Event