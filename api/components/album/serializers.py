from rest_framework import serializers
from django.template.defaultfilters import slugify

from api.components.genre.serializers import SimpleGenreSerializer

from .models import Album
from ..author import serializers as author_serializers
from ..track.serializers import SimpleTrackSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = author_serializers.ArtistSerializer(read_only=True)
    band = author_serializers.BandSerializer(read_only=True)
    tracks = SimpleTrackSerializer(many=True, read_only=True)
    genres = SimpleGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'slug',
            'release_date',
            'release_type',
            'art_cover',
            'art_cover_url',
            'artist',
            'band',
            'tracks',
            'genres',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]


class SimpleAlbumSerializer(serializers.ModelSerializer):
    artist = author_serializers.SimpleArtistSerializer(read_only=True)
    band = author_serializers.SimpleBandSerializer(read_only=True)
    genres = SimpleGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'slug',
            'release_date',
            'release_type',
            'art_cover',
            'art_cover_url',
            'artist',
            'band',
            'genres'
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class CreateAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'title',
            'release_date',
            'release_type',
            'art_cover',
            'art_cover_url',
            'artist',
            'band',
            'genres'
        ]

    def create(self, validated_data):
        # Generate a unique slug
        if not self.slug:
            count = 0
            while True:
                slug = slugify(self.title) if count == 0 else f"{slug}-{count}"
                if not Album.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                count += 1
        return super().create(validated_data)

    def save(self, **kwargs):
        # Only a band or an artist can be set as an album author
        if self.validated_data['band'] and self.validated_data['artist']:
            raise serializers.ValidationError(
                "An album can only have an artist or a band as an author, not both.")

        if not self.validated_data['band'] and not self.validated_data['artist']:
            raise serializers.ValidationError(
                "An album must have an artist or a band as an author.")

        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
