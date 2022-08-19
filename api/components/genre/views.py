from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from ...permissions import IsAuthOrReadOnly


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.select_related(
        'created_by', 'updated_by').all()
    serializer_class = serializers.GenreSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthOrReadOnly]
