from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers


class ContributorViewSet(ModelViewSet):
    queryset = models.Contributor.objects.select_related(
        'user').all()
    serializer_class = serializers.ContributorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]
