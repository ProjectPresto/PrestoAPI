from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['created_at',
                            'created_by', 'updated_at', 'updated_by']
        extra_kwargs = {
            'slug': {'required': False},
            'release_date': {'required': False},
            'release_type': {'required': False},
            'art_cover': {'required': False},
            'art_cover_url': {'required': False},
            'created_by': {'default': serializers.CurrentUserDefault()},
            'updated_by': {'default': serializers.CurrentUserDefault()},
        }
