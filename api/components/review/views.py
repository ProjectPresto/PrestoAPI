from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class ReviewViewSet(ModelViewSet):
    queryset = models.Review.objects.select_related(
        'album', 'user').all()
    serializer_class = serializers.ReviewSerializer
