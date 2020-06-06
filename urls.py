from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from events import api

router = routers.DefaultRouter()
router.register(r'events', api.EventViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('participants/', include('participants.urls')),
    path('admin/', admin.site.urls),
    path('', include('events.urls', namespace='events')),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    )
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar  # noqa: WPS433
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
