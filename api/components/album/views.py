from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from ...permissions import IsAuthSubmissionOrReadOnly
from . import models
from . import serializers


class AlbumViewSet(ModelViewSet):
    queryset = models.Album.objects.select_related(
        'artist', 'band', 'created_by', 'updated_by').all()
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_date']

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SimpleAlbumSerializer
        elif self.action in ["create", "update"]:
            return serializers.CreateAlbumSerializer
        return serializers.AlbumSerializer
