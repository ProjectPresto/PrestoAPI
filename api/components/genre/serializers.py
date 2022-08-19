from rest_framework import serializers
from django.template.defaultfilters import slugify

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
        # Generate a unique slug
        if not self.slug:
            count = 0
            while True:
                slug = slugify(self.name) if count == 0 else f"{slug}-{count}"
                if not Genre.objects.filter(slug=slug).exists():
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
