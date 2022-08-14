from rest_framework.viewsets import ModelViewSet
from .models import Artist, Band
from .serializers import ArtistSerializer, BandSerializer
from ...permissions import IsAuthSubmissionOrReadOnly


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.select_related('created_by', 'updated_by').all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]


class BandViewSet(ModelViewSet):
    queryset = Band.objects.select_related('created_by', 'updated_by').all()
    serializer_class = BandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
