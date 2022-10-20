from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Artist, Band, BandMember
from . import serializers
from ...permissions import IsAuthSubmissionOrReadOnly


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.select_related('created_by', 'updated_by').all()
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'birth_date': ['day__exact', 'month__exact'],
        'death_date': ['day__exact', 'month__exact'],
        'album__genres': ['exact'],
    }
    ordering_fields = ['name', 'birth_date']
    search_fields = ['name', 'slug', 'album__title']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SimpleArtistSerializer
        return serializers.ArtistSerializer


class BandViewSet(ModelViewSet):
    queryset = Band.objects.select_related('created_by', 'updated_by').all()
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'album__genres': ['exact'],
    }
    ordering_fields = ['name', 'founding_year']
    search_fields = ['name', 'slug', 'album__title']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SimpleBandSerializer
        return serializers.BandSerializer


class BandMemberViewSet(ModelViewSet):
    queryset = BandMember.objects.select_related(
        'band', 'artist', 'created_by', 'updated_by').all()
    permission_classes = [IsAuthSubmissionOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateBandMemberSerializer
        return serializers.BandMemberSerializer
