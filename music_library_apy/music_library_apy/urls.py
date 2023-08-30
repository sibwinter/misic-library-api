from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'songs', views.SongViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Music library API",
      default_version='v1',
      description="Библиотека исполнителей и их альбомов",
      contact=openapi.Contact(email="sibwinter42@yandex.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
