from rest_framework import serializers, fields
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Advert, Category, Contact, Publication
from drf_extra_fields.fields import Base64FileField
import base64
from django.core.files.base import ContentFile

User = get_user_model()

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str))

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
    featured_image = Base64FileField()
    published_date = fields.DateTimeField(input_formats=['%Y-%m-%d:%H:%M:%S'], required=False)
    category = CategorySerializer(required=False)
    view_count = fields.IntegerField(source='get_count', required=False)

    class Meta:
        fields = "__all__"
        model = Post

    def save(self, **kwargs):
        self.featured_image = base64_file(self.featured_image)
        
        return super(PostSerializer, self).save(**kwargs)

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
    photo = Base64FileField()
    class Meta:
        fields = '__all__'
        model = Advert

    def save(self, **kwargs):
        self.photo = Advert.objects.create(base64_file(self.photo))
        
        return super(AdvertSerializer, self).save(**kwargs)

class PublicationSerializer(serializers.ModelSerializer):
    photo = Base64FileField()
    class Meta:
        fields = '__all__'
        model = Publication

    def save(self, **kwargs):
        self.photo = Publication.objects.create(base64_file(self.photo))
        
        return super(PostSerializer, self).save(**kwargs)