from rest_framework import serializers
from .models import FeaturedAuthor, Track
from api.components.author.serializers import SimpleArtistSerializer, SimpleBandSerializer
from api.helpers.UniqueSlug import createUniqueSlug, updateUniqueSlug


class SimpleFeaturedAuthorSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer(read_only=True)
    band = SimpleBandSerializer(read_only=True)

    class Meta:
        model = FeaturedAuthor
        fields = [
            'id',
            'track',
            'artist',
            'band'
        ]


class FeaturedAuthorSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer()
    band = SimpleBandSerializer()

    class Meta:
        model = FeaturedAuthor
        fields = [
            'id',
            'track',
            'artist',
            'band',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleTrackSerializer(serializers.ModelSerializer):
    featured_authors = SimpleFeaturedAuthorSerializer(
        many=True, read_only=True)

    class Meta:
        model = Track
        fields = [
            'id',
            'title',
            'slug',
            'position',
            'disc',
            'duration',
            'featured_authors'
        ]


class TrackSerializer(serializers.ModelSerializer):
    featured_authors = FeaturedAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = [
            'id',
            'title',
            'slug',
            'position',
            'disc',
            'duration',
            'featured_authors',
            'album',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        read_only_fields = ['slug', 'created_by', 'updated_by']

    def create(self, validated_data):
        validated_data = createUniqueSlug(Track, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = updateUniqueSlug(Track, instance, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
