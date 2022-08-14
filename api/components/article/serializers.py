from rest_framework import serializers

from .models import AlbumArticle, ArtistArticle, BandArticle, TrackArticle


class AlbumArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return AlbumArticle.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class ArtistArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return ArtistArticle.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class BandArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return BandArticle.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )


class TrackArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackArticle
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']

    def create(self, validated_data):
        # Get user from jwt header
        user = self.context['request'].user
        return TrackArticle.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data
        )
