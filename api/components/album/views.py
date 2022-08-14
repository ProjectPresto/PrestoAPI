from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class AlbumViewSet(ModelViewSet):
    queryset = models.Album.objects.select_related(
        'artist', 'band', 'created_by', 'updated_by').all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SimpleAlbumSerializer
        elif self.action == "create":
            return serializers.CreateAlbumSerializer
        return serializers.AlbumSerializer
