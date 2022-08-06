from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("album", views.AlbumViewSet, basename="album")

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
