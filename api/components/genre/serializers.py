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
        read_only_fields = ['slug', 'created_at',
                            'updated_at', 'created_by', 'updated_by']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return Genre.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class AlbumGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumGenre
        fields = ['id', 'album', 'genre']
