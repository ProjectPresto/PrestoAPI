from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from ...permissions import IsAuthOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.select_related(
        'created_by', 'updated_by').all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [IsAuthOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'id': ['in'],
        'name': ['icontains'],
    }
    search_fields = ['name']
