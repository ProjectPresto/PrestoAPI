from rest_framework.viewsets import ModelViewSet
from .models import Track
from .serializers import TrackSerializer


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.select_related(
        'album_id', 'created_by', 'updated_by').all()
    serializer_class = TrackSerializer
    lookup_field = 'slug'
