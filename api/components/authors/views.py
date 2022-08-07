from rest_framework.viewsets import ModelViewSet
from .models import Artist, Band
from .serializers import ArtistSerializer, BandSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'


class BandViewSet(ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    lookup_field = 'slug'
