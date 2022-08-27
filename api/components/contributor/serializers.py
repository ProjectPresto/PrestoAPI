from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        model = Contributor
        fields = '__all__'

    def save(self, **kwargs):
        # Check if the user is accessing his/her own profile or is a superuser
        if self.context['request'].user.id == self.validated_data['user'].id or self.context['request'].user.is_superuser:
            return super().save(**kwargs)
        else:
            raise serializers.ValidationError(
                'You are not allowed to edit this profile')
