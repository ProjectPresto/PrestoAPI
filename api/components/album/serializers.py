import datetime
import logging
import sys

from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.db.models.fields import DurationField
from django.db.models import Sum, ExpressionWrapper
from django.db.models.expressions import F
from api.components.article.serializers import AlbumArticleSerializer

from api.components.genre.serializers import SimpleGenreSerializer
from api.components.track.models import Track
from api.helpers.UniqueSlug import createUniqueSlug, updateUniqueSlug

from .models import Album
from ..author import serializers as author_serializers
from ..track.serializers import SimpleTrackSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = author_serializers.ArtistSerializer(read_only=True)
    band = author_serializers.BandSerializer(read_only=True)
    tracks = SimpleTrackSerializer(many=True, read_only=True)
    genres = SimpleGenreSerializer(many=True, read_only=True)
    article = AlbumArticleSerializer(source="albumarticle", read_only=True)
    full_duration = serializers.SerializerMethodField()

    def get_full_duration(self, obj):
        tracks_dur = Track.objects.filter(
            album_id=obj.id).all().aggregate(res=Sum('duration'))['res']
        if tracks_dur is not None:
            return str(tracks_dur)
        return tracks_dur

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
            'full_duration',
            'tracks',
            'genres',
            'article',
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
        validated_data = createUniqueSlug(Album, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = updateUniqueSlug(Album, instance, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Populate empty band and artist
        if 'band' not in self.validated_data:
            self.validated_data['band'] = self.instance.band

        if 'artist' not in self.validated_data:
            self.validated_data['artist'] = self.instance.artist

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
