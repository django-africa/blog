from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
# from django.contrib.staticfiles import views
# from django.urls import re_path
from .views import UserViewSet, PostViewSet, AdvertViewSet, ContactViewSet, CommentViewSet, PrayerRequestViewSet, CategoryViewSet, PublicationViewSet, MinistriesViewset

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
router.register('prayer_request', PrayerRequestViewSet, basename='prayer_request')
router.register('category', CategoryViewSet, basename='category'),
router.register('contact', ContactViewSet, basename='contact'),
router.register('advert', AdvertViewSet, basename='category'),
router.register('publication', PublicationViewSet, basename='publication')
router.register('ministries', MinistriesViewset, basename='ministries')

urlpatterns = [
    
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
