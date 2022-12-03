from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
from ...permissions import IsAuthOrReadOnly

class AlbumServiceLinkViewSet(ModelViewSet):
    queryset = models.AlbumServiceLink.objects.select_related(
        'album', 'created_by', 'updated_by').all()
    serializer_class = serializers.AlbumServiceLinkSerializer
    permission_classes = [IsAuthOrReadOnly]

class ArtistServiceLinkViewSet(ModelViewSet):
    queryset = models.ArtistServiceLink.objects.select_related(
        'artist', 'created_by', 'updated_by').all()
    serializer_class = serializers.ArtistServiceLinkSerializer
    permission_classes = [IsAuthOrReadOnly]

class BandServiceLinkViewSet(ModelViewSet):
    queryset = models.BandServiceLink.objects.select_related(
        'band', 'created_by', 'updated_by').all()
    serializer_class = serializers.BandServiceLinkSerializer
    permission_classes = [IsAuthOrReadOnly]