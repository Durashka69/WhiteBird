# from rest_framework.routers import SimpleRouter

# from .views import VideoViewSet


# router = SimpleRouter()

# router.register('api/videos', VideoViewSet, basename='api/videos')
from django.urls import path

from .views import VideoImageAPIView


urlpatterns = [
    path('api/gallery/', VideoImageAPIView.as_view(), name="gallery-list"),
]
