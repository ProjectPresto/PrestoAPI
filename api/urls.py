from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from .components.album import views as album_views
from .components.author import views as author_views
from .components.track import views as track_views

router = routers.DefaultRouter()
router.register('album', album_views.AlbumViewSet, basename='album')
router.register('track', track_views.TrackViewSet, basename='track')
router.register('artist', author_views.ArtistViewSet, basename='artist')
router.register('band', author_views.BandViewSet, basename='band')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
