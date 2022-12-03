from rest_framework import serializers

from . import models


class AlbumServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumServiceLink
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)

class SimpleAlbumServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumServiceLink
        fields = [
            'link',
            'service'
        ]

class ArtistServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtistServiceLink
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleArtistServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtistServiceLink
        fields = [
            'link',
            'service'
        ]


class BandServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BandServiceLink
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)

class SimpleBandServiceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BandServiceLink
        fields = [
            'link',
            'service'
        ]