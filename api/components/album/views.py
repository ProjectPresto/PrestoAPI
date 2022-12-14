from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ...permissions import IsAuthSubmissionOrReadOnly
from . import models
from . import serializers


class AlbumViewSet(ModelViewSet):
    queryset = models.Album.objects.select_related(
        'artist', 'band', 'albumarticle', 'created_by', 'updated_by'
    ).prefetch_related(
        'tracks', 'genres', 'tracks__featured_authors'
    ).all()
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'artist': ['exact'],
        'band': ['exact'],
        'release_type': ['exact'],
        'genres': ['exact'],
        'release_date': ['gte', 'lte', 'day__exact', 'month__exact'],
    }
    ordering_fields = ['title', 'release_date', 'created_at']
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SimpleAlbumSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return serializers.CreateAlbumSerializer
        return serializers.AlbumSerializer
