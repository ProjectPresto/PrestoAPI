from rest_framework import serializers

from api.components.album.models import Album
from api.components.article.serializers import ArtistArticleSerializer, BandArticleSerializer
from api.helpers.UniqueSlug import createUniqueSlug, updateUniqueSlug

from .models import Artist, Band, BandMember

from .helpers import getGenres
from ..genre.serializers import SimpleGenreSerializer
from ..serviceLink.serializers import SimpleArtistServiceLinkSerializer, SimpleBandServiceLinkSerializer


class AlbumInAuthorSerializer(serializers.ModelSerializer):
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
            'genres'
        ]


class SimpleArtistSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'artist')

    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'slug',
            'bg_image',
            'bg_image_url',
            'birth_date',
            'death_date',
            'genres',
        ]


class BandMemberSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer()

    class Meta:
        model = BandMember
        fields = [
            'id',
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


class BandSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()
    band_members = serializers.SerializerMethodField()
    article = BandArticleSerializer(source="bandarticle", read_only=True)
    serviceLinks = SimpleBandServiceLinkSerializer(source="band_service_links", read_only=True, many=True)

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'band')

    def get_band_members(self, obj):
        request = self.context.get('request')
        band_members = obj.bandmember_set.order_by('join_year').all()
        return BandMemberSerializer(band_members, many=True, read_only=True, context={'request': request}).data

    def get_albums(self, obj):
        request = self.context.get('request')
        albums = obj.album_set.order_by('-release_date').all()
        return AlbumInAuthorSerializer(albums, many=True, read_only=True, context={'request': request}).data

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
            'albums',
            'article',
            'serviceLinks',
            'band_members',
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
        validated_data = updateUniqueSlug(Band, instance, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleBandSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'band')

    class Meta:
        model = Band
        fields = [
            'id',
            'name',
            'slug',
            'bg_image',
            'bg_image_url',
            'genres',
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


class ArtistMembershipSerializer(serializers.ModelSerializer):
    band = SimpleBandSerializer()

    class Meta:
        model = BandMember
        fields = [
            'id',
            'band',
            'join_year',
            'quit_year',
            'roles'
        ]


class ArtistSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()
    band_memberships = serializers.SerializerMethodField()
    article = ArtistArticleSerializer(source="artistarticle", read_only=True)
    serviceLinks = SimpleArtistServiceLinkSerializer(source="artist_service_links", read_only=True, many=True)

    def get_albums(self, obj):
        request = self.context.get('request')
        albums = obj.album_set.order_by('-release_date').all()
        return AlbumInAuthorSerializer(albums, many=True, read_only=True, context={'request': request}).data

    def get_genres(self, obj):
        return getGenres.get_genres(self, obj, 'artist')

    def get_band_memberships(self, obj):
        request = self.context.get('request')
        band_memberships = obj.bandmember_set.order_by('-join_year').all()
        return ArtistMembershipSerializer(band_memberships, many=True, read_only=True,
                                          context={'request': request}).data

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
            'albums',
            'article',
            'serviceLinks',
            'band_memberships',
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
        validated_data = updateUniqueSlug(Artist, instance, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user

        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
