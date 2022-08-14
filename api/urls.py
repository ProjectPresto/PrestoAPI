from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from .components.album import views as album_views
from .components.author import views as author_views
from .components.track import views as track_views
from .components.genre import views as genre_views
from .components.review import views as review_views

router = routers.DefaultRouter()

# ALBUM
router.register('album', album_views.AlbumViewSet, basename='album')

# AUTHOR
router.register('artist', author_views.ArtistViewSet, basename='artist')
router.register('band', author_views.BandViewSet, basename='band')

# TRACK
router.register('track', track_views.TrackViewSet, basename='track')
router.register(
    'featured-author', track_views.FeaturedAuthorViewSet, basename='featured-author')

# GENRE
router.register('genre', genre_views.GenreViewSet, basename='genre')
router.register('album-genre', genre_views.AlbumGenreViewSet,
                basename='album-genre')

# REVIEW
router.register('review', review_views.ReviewViewSet, basename='review')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
