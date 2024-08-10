from .views import ArtistAPITelegramViewSet, AlbumAPITelegramViewSet, SongAPITelegramViewSet
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Spotify API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'song', SongAPITelegramViewSet, basename='song')
router.register(r'album', AlbumAPITelegramViewSet, basename='album')
router.register(r'artist', ArtistAPITelegramViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
