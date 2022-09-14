from rest_framework import serializers

from .models import AlbumArticle, ArtistArticle, BandArticle, TrackArticle


class AlbumArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'album__slug'
        extra_kwargs = {
            'url': {'lookup_field': 'album__slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class ArtistArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'artist__slug'
        extra_kwargs = {
            'url': {'lookup_field': 'artist__slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class BandArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'band__slug'
        extra_kwargs = {
            'url': {'lookup_field': 'band__slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class TrackArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'track__slug'
        extra_kwargs = {
            'url': {'lookup_field': 'track__slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
