from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'songs', views.SongViewSet)

schema_view = get_swagger_view(title='SWAGGER API')

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
