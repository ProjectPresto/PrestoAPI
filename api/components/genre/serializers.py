from rest_framework import serializers

from api.components.album.models import Album
from api.components.author.models import Artist, Band
from api.helpers.unique_slug import create_unique_slug, update_unique_slug
from .models import Genre


class SimpleGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    album_count = serializers.SerializerMethodField()
    artist_count = serializers.SerializerMethodField()
    band_count = serializers.SerializerMethodField()

    def get_album_count(self, obj):
        return Album.objects.filter(genres__id=obj.id).distinct('pk').count()

    def get_artist_count(self, obj):
        return Artist.objects.filter(album__genres__id=obj.id).distinct('pk').count()

    def get_band_count(self, obj):
        return Band.objects.filter(album__genres__id=obj.id).distinct('pk').count()

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['slug', 'created_by', 'updated_by']

    def create(self, validated_data):
        validated_data = create_unique_slug(Genre, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = update_unique_slug(Genre, instance, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
