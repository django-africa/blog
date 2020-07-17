from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
from .tasks import send_feedback_email_task, recolor_blog_picture_task# Create your models here.


class UserProfile(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    profile_image = models.FileField(upload_to="profile_pic", blank=True, null=True)

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Post(models.Model, HitCountMixin):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=350, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    view_count = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    featured_image = models.FileField(upload_to='images/', null=True, blank=True)
    summary = models.CharField(max_length=100, default='', null=True, blank=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-id']

    def get_author_name(self):
        return self.author.get_full_name()

    def get_post_summary(self):
        self.summary = self.text[:100]
        return self.summary

    def get_count(self):
        return self.hit_count.hits

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.summary = self.get_post_summary()
        # recolor_blog_picture_task.apply_async(self.featured_image)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def anonymous_user(self):
        if self.user is None:
            self.user.full_name = "Anonymous"
            self.user.profile_image = models.FileField(default="default.png")

    def __str__(self):
        return '{} comment made by {}'.format(self.body, self.get_name)


class PrayerRequest(models.Model):
    name = models.CharField(max_length=350)
    email = models.EmailField()
    prayer_point = models.TextField()
    date = models.DateTimeField(blank=True, null=True,)

    class Meta:
        ordering = ['-date']    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        # message = "Hi, {}. Your prayer request has been successfully sent across. " \
        #           "You are in our prayers.".format(self.name)
        # send_feedback_email_task.apply_async(message, self.email)

        # use signal to send the message after the request has been created
        return super(PrayerRequest, self).save(*args, **kwargs)

class Contact(models.Model):
    fullname = models.CharField(max_length=200);
    phonenumber = models.IntegerField(null=True, blank=True);
    address = models.CharField(max_length=350);
    message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True);

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(Contact, self).save(*args, **kwargs)