from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.yasg import urlpatterns as docs_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.events.urls')),
    path("", include("apps.reqs.urls")),
    path('', include('apps.posts.urls')),
    path('', include('apps.videos.urls'))
]


urlpatterns += docs_urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
