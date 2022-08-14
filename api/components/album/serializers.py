from rest_framework import serializers

from .models import Album
from ..author.serializers import ArtistSerializer, BandSerializer
from ..track.serializers import SimpleTrackSerializer
from ..genre.serializers import SimpleGenreSerializer


class SimpleAlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    band = BandSerializer(read_only=True)

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
        ]

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return Album.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    band = BandSerializer(read_only=True)
    tracks = SimpleTrackSerializer(many=True, read_only=True)
    genres = serializers.StringRelatedField(
        many=True, read_only=True, source='album_genres')

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
