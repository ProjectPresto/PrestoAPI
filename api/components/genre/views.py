from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.select_related(
        'created_by', 'updated_by').all()
    serializer_class = serializers.GenreSerializer
    lookup_field = 'slug'


class AlbumGenreViewSet(ModelViewSet):
    queryset = models.AlbumGenre.objects.select_related(
        'album', 'genre', 'created_by', 'updated_by').all()
    serializer_class = serializers.AlbumGenreSerializer
