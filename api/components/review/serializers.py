from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

    def save(self, **kwargs):
        if self.context['request'].user.id == self.validated_data['user'].id or self.context['request'].user.is_superuser:
            return super().save(**kwargs)
        else:
            raise serializers.ValidationError(
                "You can only create/edit your own reviews")
