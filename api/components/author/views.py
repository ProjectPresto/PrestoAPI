from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Artist, Band, BandMember
from .serializers import ArtistSerializer, BandSerializer, BandMemberSerializer, CreateBandMemberSerializer
from ...permissions import IsAuthSubmissionOrReadOnly


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.select_related('created_by', 'updated_by').all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'birth_date': ['day__exact', 'month__exact'],
        'death_date': ['day__exact', 'month__exact'],
    }
    ordering_fields = ['name', 'birth_date']
    search_fields = ['name', 'album__title']


class BandViewSet(ModelViewSet):
    queryset = Band.objects.select_related('created_by', 'updated_by').all()
    serializer_class = BandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'founding_year']
    search_fields = ['name', 'album__title']


class BandMemberViewSet(ModelViewSet):
    queryset = BandMember.objects.select_related(
        'band', 'artist', 'created_by', 'updated_by').all()
    permission_classes = [IsAuthSubmissionOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBandMemberSerializer
        return BandMemberSerializer
