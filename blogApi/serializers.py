from rest_framework import serializers, fields
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Comment, UserProfile, PrayerRequest, Category
from .tasks import send_feedback_email_task


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class PostSerializer(serializers.ModelSerializer, TaggitSerializer):
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

    def save(self, *args, **kwargs):
        message = "Hi, {}. Your prayer request has been successfully sent across. " \
                  "You are in our prayers.".format(self.name)

        send_feedback_email_task(message, self.email)
        send_feedback_email_task.apply_async()
        super(PrayerRequestSerilizer, self).save(*args, **kwargs) # Call the real save() method
