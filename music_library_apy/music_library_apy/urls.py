from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]