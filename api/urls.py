from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from .components.contributor import views as contributor_views
from .components.album import views as album_views
from .components.author import views as author_views
from .components.track import views as track_views
from .components.genre import views as genre_views
from .components.review import views as review_views
from .components.article import views as article_views
from .components.serviceLink import views as service_link_views

router = routers.DefaultRouter()

# CONTRIBUTOR
router.register(
    'contributor', contributor_views.ContributorViewSet, basename='contributor')

# ALBUM
router.register('album', album_views.AlbumViewSet, basename='album')

# AUTHOR
router.register('artist', author_views.ArtistViewSet, basename='artist')
router.register('band', author_views.BandViewSet, basename='band')
router.register('band-member', author_views.BandMemberViewSet,
                basename='band-member')

# TRACK
router.register('track', track_views.TrackViewSet, basename='track')
router.register(
    'featured-author', track_views.FeaturedAuthorViewSet, basename='featured-author')

# GENRE
router.register('genre', genre_views.GenreViewSet, basename='genre')

# REVIEW
router.register('review', review_views.ReviewViewSet, basename='review')

# ARTICLE
router.register('album-article', article_views.AlbumArticleViewSet,
                basename='album-article')
router.register('artist-article', article_views.ArtistArticleViewSet,
                basename='artist-article')
router.register('band-article', article_views.BandArticleViewSet,
                basename='band-article')
router.register('track-article', article_views.TrackArticleViewSet,
                basename='track-article')

# SERVICE LINK
router.register('album-service-link', service_link_views.AlbumServiceLinkViewSet,
                basename='album-service-link')
router.register('artist-service-link', service_link_views.ArtistServiceLinkViewSet,
                basename='artist-service-link')
router.register('band-service-link', service_link_views.BandServiceLinkViewSet,
                basename='band-service-link')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
