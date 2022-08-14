from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class AlbumArticleViewSet(ModelViewSet):
    queryset = models.AlbumArticle.objects.select_related(
        'album', 'created_by', 'updated_by').all()
    serializer_class = serializers.AlbumArticleSerializer


class ArtistArticleViewSet(ModelViewSet):
    queryset = models.ArtistArticle.objects.select_related(
        'artist', 'created_by', 'updated_by').all()
    serializer_class = serializers.ArtistArticleSerializer


class BandArticleViewSet(ModelViewSet):
    queryset = models.BandArticle.objects.select_related(
        'band', 'created_by', 'updated_by').all()
    serializer_class = serializers.BandArticleSerializer


class TrackArticleViewSet(ModelViewSet):
    queryset = models.TrackArticle.objects.select_related(
        'track', 'created_by', 'updated_by').all()
    serializer_class = serializers.TrackArticleSerializer
