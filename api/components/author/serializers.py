from rest_framework import serializers
from django.template.defaultfilters import slugify
from api.helpers.UniqueSlug import createUniqueSlug, updateUniqueSlug

from .models import Artist, Band, BandMember

from .helpers import getGenres


class ArtistSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'artist')

    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'slug',
            'full_name',
            'birth_date',
            'death_date',
            'bg_image',
            'bg_image_url',
            'genres',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        read_only_fields = [
            'slug',
            'created_by',
            'updated_by',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def create(self, validated_data):
        validated_data = createUniqueSlug(Artist, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = updateUniqueSlug(Artist, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user

        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'slug',
            'bg_image',
            'bg_image_url',
        ]


class BandSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'band')

    class Meta:
        model = Band
        fields = [
            'id',
            'name',
            'slug',
            'founding_year',
            'breakup_year',
            'bg_image',
            'bg_image_url',
            'genres',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        read_only_fields = [
            'slug',
            'created_by',
            'updated_by',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def create(self, validated_data):
        validated_data = createUniqueSlug(Band, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = updateUniqueSlug(Band, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = [
            'id',
            'name',
            'slug',
            'bg_image',
            'bg_image_url',
        ]


class BandMemberSerializer(serializers.ModelSerializer):
    band = BandSerializer()
    artist = ArtistSerializer()

    class Meta:
        model = BandMember
        fields = [
            'id',
            'band',
            'artist',
            'name',
            'roles',
            'join_year',
            'quit_year',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
        ]


class CreateBandMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandMember
        fields = [
            'band',
            'artist',
            'name',
            'roles',
            'join_year',
            'quit_year',
        ]

    def save(self, **kwargs):
        if not self.validated_data['artist'] and not self.validated_data['name']:
            raise serializers.ValidationError(
                "Artist or name must be specified")
        if self.validated_data['artist'] and self.validated_data['name']:
            raise serializers.ValidationError(
                "Artist or name must be specified, not both")

        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
