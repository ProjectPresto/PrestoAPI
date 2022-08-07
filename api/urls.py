from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from .components.album.views import AlbumViewSet
from .components.authors.views import ArtistViewSet, BandViewSet

router = routers.DefaultRouter()
router.register("album", AlbumViewSet, basename="album")
router.register("artist", ArtistViewSet, basename="artist")
router.register("band", BandViewSet, basename="band")

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
