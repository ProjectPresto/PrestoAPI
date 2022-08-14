from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
from ...permissions import IsAuthSubmissionOrReadOnly


class TrackViewSet(ModelViewSet):
    queryset = models.Track.objects.select_related(
        'album', 'created_by', 'updated_by').all()
    permission_classes = [IsAuthSubmissionOrReadOnly]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SimpleTrackSerializer
        return serializers.TrackSerializer


class FeaturedAuthorViewSet(ModelViewSet):
    queryset = models.FeaturedAuthor.objects.select_related(
        'track', 'artist', 'band', 'created_by', 'updated_by').all()
    serializer_class = serializers.FeaturedAuthorSerializer
    permission_classes = [IsAuthSubmissionOrReadOnly]
