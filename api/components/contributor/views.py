from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class ContributorViewSet(ModelViewSet):
    queryset = models.Contributor.objects.select_related(
        'user').all()
    lookup_field = 'user'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'user': ['exact'],
        'user__username': ['icontains'],
    }

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.ContributorSerializer
        return serializers.SimpleContributorSerializer

    @action(detail=True, methods=['get'])
    def simple(self, request, pk=None, *args, **kwargs):
        contributor = self.get_object()
        serializer = self.get_serializer(contributor)
        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_400_BAD_REQUEST)
