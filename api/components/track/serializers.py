from rest_framework import serializers
from django.template.defaultfilters import slugify

from .models import FeaturedAuthor, Track


class FeaturedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedAuthor
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

    def save(self, **kwargs):
        # Get user from JWT header
        user = self.context['request'].user
        if self.instance is None:
            return super().save(created_by=user, updated_by=user, **kwargs)
        else:
            return super().save(updated_by=user, **kwargs)


class SimpleTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'id',
            'title',
            'slug',
            'position',
            'duration',
        ]


class TrackSerializer(serializers.ModelSerializer):
    featured_authors = FeaturedAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['slug', 'created_by', 'updated_by']

    def create(self, validated_data):
        # Generate a unique slug
        if not self.slug:
            count = 0
            while True:
                slug = slugify(self.title) if count == 0 else f"{slug}-{count}"
                if not Track.objects.filter(slug=slug).exists():
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
