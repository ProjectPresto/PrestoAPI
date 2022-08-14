from rest_framework import serializers
from . import models


class FeaturedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeaturedAuthor
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'created_by': {'default': serializers.CurrentUserDefault()},
            'updated_by': {'default': serializers.CurrentUserDefault()},
        }

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return models.FeaturedAuthor.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class SimpleTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = [
            'id',
            'title',
            'slug',
            'position',
            'duration',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class TrackSerializer(serializers.ModelSerializer):
    featured_authors = FeaturedAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = models.Track
        fields = '__all__'
        read_only_fields = [
            'slug',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return models.Track.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )
