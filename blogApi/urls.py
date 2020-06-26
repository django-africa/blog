from django.urls import path
from django.conf import settings
from rest_framework.routers import SimpleRouter
from django.conf.urls.static import static
from .views import UserViewSet, PostViewSet, CommentViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
