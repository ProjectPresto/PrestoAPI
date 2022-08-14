from rest_framework import serializers
from django.template.defaultfilters import slugify

from .models import Artist, Band, BandMember


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
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
        # Generate a unique slug
        if not self.slug:
            count = 0
            while True:
                slug = slugify(self.name) if count == 0 else f"{slug}-{count}"
                if not Artist.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                count += 1
        return super().create(validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'
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
        # Generate a unique slug
        if not self.slug:
            count = 0
            while True:
                slug = slugify(self.name) if count == 0 else f"{slug}-{count}"
                if not Band.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                count += 1
        return super().create(validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


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
