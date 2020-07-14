from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from events import api as events_api
from accounts import api as accounts_api

router = routers.DefaultRouter()
router.register(r'events', events_api.EventViewSet)
router.register(r'register', accounts_api.UserViewSet, basename='register')


urlpatterns = [
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token-obtain-pair',
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh',
    ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
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
