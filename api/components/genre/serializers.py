from rest_framework import serializers
from django.template.defaultfilters import slugify

from api.helpers.UniqueSlug import createUniqueSlug, updateUniqueSlug

from .models import Genre


class SimpleGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['slug', 'created_by', 'updated_by']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def create(self, validated_data):
        validated_data = createUniqueSlug(Genre, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = updateUniqueSlug(Genre, validated_data)
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)
