from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
from ...permissions import IsAuthSubmissionOrReadOnly


class AlbumArticleViewSet(ModelViewSet):
    queryset = models.AlbumArticle.objects.select_related(
        'album', 'created_by', 'updated_by').all()
    lookup_field = 'album__slug'
    serializer_class = serializers.AlbumArticleSerializer
    permission_classes = [IsAuthSubmissionOrReadOnly]


class ArtistArticleViewSet(ModelViewSet):
    queryset = models.ArtistArticle.objects.select_related(
        'artist', 'created_by', 'updated_by').all()
    lookup_field = 'artist__slug'
    serializer_class = serializers.ArtistArticleSerializer
    permission_classes = [IsAuthSubmissionOrReadOnly]


class BandArticleViewSet(ModelViewSet):
    queryset = models.BandArticle.objects.select_related(
        'band', 'created_by', 'updated_by').all()
    lookup_field = 'band__slug'
    serializer_class = serializers.BandArticleSerializer
    permission_classes = [IsAuthSubmissionOrReadOnly]


class TrackArticleViewSet(ModelViewSet):
    queryset = models.TrackArticle.objects.select_related(
        'track', 'created_by', 'updated_by').all()
    lookup_field = 'track__slug'
    serializer_class = serializers.TrackArticleSerializer
    permission_classes = [IsAuthSubmissionOrReadOnly]
