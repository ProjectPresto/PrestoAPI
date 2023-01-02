from rest_framework import serializers

from api.helpers.get_contributions_objects import get_contributions_objects
from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    contributions = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_contributions(self, obj):
        return get_contributions_objects(obj.user)

    class Meta:
        model = Contributor
        fields = [
            'id',
            'username',
            'email',
            'about_text',
            'profile_picture',
            'profile_picture_url',
            'user',
            'contributions'
        ]
        lookup_field = 'user'
        extra_kwargs = {
            'url': {'lookup_field': 'user'},
        }


class SimpleContributorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    contributions_count = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_contributions_count(self, obj):
        return get_contributions_objects(obj.user)['counts']

    class Meta:
        model = Contributor
        fields = '__all__'

    def save(self, **kwargs):
        # Check if the user is accessing his/her own profile or is a superuser
        if self.context['request'].user.id == self.validated_data['user'].id or self.context[
            'request'].user.is_superuser:
            return super().save(**kwargs)
        else:
            raise serializers.ValidationError(
                'You are not allowed to edit this profile')
