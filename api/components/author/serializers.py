from rest_framework import serializers
from .models import Artist, Band


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
        # Get user from jwt header
        user = self.context['request'].user
        return Artist.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


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
        # Get user from jwt header
        user = self.context['request'].user
        return Band.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )
