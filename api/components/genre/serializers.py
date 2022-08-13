from rest_framework import serializers

from .models import Genre, AlbumGenre
# from ..album.serializers import SimpleAlbumSerializer


class SimpleGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = [
            'slug',
            'created_at',
            'updated_at',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class AlbumGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumGenre
        fields = ['id', 'album', 'genre']
