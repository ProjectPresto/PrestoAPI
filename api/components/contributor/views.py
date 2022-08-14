from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class ContributorViewSet(ModelViewSet):
    queryset = models.Contributor.objects.select_related(
        'user').all()
    serializer_class = serializers.ContributorSerializer
