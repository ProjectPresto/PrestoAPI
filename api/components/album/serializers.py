from rest_framework import serializers
from .models import Album
from ..author.serializers import ArtistSerializer, BandSerializer
from ..track.serializers import SimpleTrackSerializer


class SimpleAlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(source="artist_id", read_only=True)
    band = BandSerializer(source="band_id", read_only=True)

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


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(source="artist_id", read_only=True)
    band = BandSerializer(source="band_id", read_only=True)
    tracks = SimpleTrackSerializer(many=True, read_only=True)

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
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]
        read_only_fields = [
            'slug',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'created_by': {'default': serializers.CurrentUserDefault()},
            'updated_by': {'default': serializers.CurrentUserDefault()},
        }
