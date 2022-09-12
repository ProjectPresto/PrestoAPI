from rest_framework.viewsets import ModelViewSet
from .models import Artist, Band, BandMember
from .serializers import ArtistSerializer, BandSerializer, BandMemberSerializer, CreateBandMemberSerializer
from ...permissions import IsAuthSubmissionOrReadOnly
from rest_framework.filters import OrderingFilter


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.select_related('created_by', 'updated_by').all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'birth_date']


class BandViewSet(ModelViewSet):
    queryset = Band.objects.select_related('created_by', 'updated_by').all()
    serializer_class = BandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthSubmissionOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'founding_year']


class BandMemberViewSet(ModelViewSet):
    queryset = BandMember.objects.select_related(
        'band', 'artist', 'created_by', 'updated_by').all()
    permission_classes = [IsAuthSubmissionOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBandMemberSerializer
        return BandMemberSerializer
