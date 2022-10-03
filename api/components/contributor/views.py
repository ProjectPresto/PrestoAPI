from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers


class ContributorViewSet(ModelViewSet):
    queryset = models.Contributor.objects.select_related(
        'user').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'user': ['exact'],
        'user__username': ['icontains'],
    }

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.ContributorSerializer
        return serializers.SimpleContributorSerializer
