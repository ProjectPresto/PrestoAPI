from rest_framework.viewsets import ModelViewSet
from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.select_related(
        'artist_id', 'band_id', 'created_by', 'updated_by').all()
    serializer_class = AlbumSerializer
    lookup_field = 'slug'
