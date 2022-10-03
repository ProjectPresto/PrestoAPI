import operator
from rest_framework import serializers
from rest_framework.settings import api_settings

from api.components.album.models import Album
from api.components.author.models import Artist, Band, BandMember
from api.components.genre.models import Genre
from api.components.track.models import Track

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    contributions = serializers.SerializerMethodField()

    def get_contributions(self, obj):
        createdAlbums = Album.objects.filter(
            created_by=obj.user).values('title', 'slug', 'artist__name', 'artist__slug', 'band__name', 'band__slug', 'created_at')

        createdTracks = Track.objects.filter(
            created_by=obj.user).values('title', 'slug', 'album__title', 'album__slug', 'created_at')

        createdArtists = Artist.objects.filter(
            created_by=obj.user).values('name', 'slug', 'created_at')

        createdBands = Band.objects.filter(
            created_by=obj.user).values('name', 'slug', 'created_at')

        createdGenres = Genre.objects.filter(
            created_by=obj.user).values('name', 'slug', 'created_at')

        createdBandMembers = BandMember.objects.filter(
            created_by=obj.user).values('artist__name', 'artist__slug', 'name', 'band__name', 'band__slug', 'created_at')

        for album in createdAlbums:
            album['type'] = 'Album'

        for track in createdTracks:
            track['type'] = 'Track'

        for artist in createdArtists:
            artist['type'] = 'Artist'

        for band in createdBands:
            band['type'] = 'Band'

        for genre in createdGenres:
            genre['type'] = 'Genre'

        for bandMember in createdBandMembers:
            bandMember['type'] = 'BandMember'

        data = list(createdAlbums) + list(createdTracks) + list(createdArtists) + \
            list(createdBands) + list(createdGenres) + list(createdBandMembers)

        data.sort(key=operator.itemgetter('created_at'), reverse=True)

        return {
            'counts': {
                'createdAlbums': createdAlbums.count(),
                'createdTracks': createdTracks.count(),
                'createdArtists': createdArtists.count(),
                'createdBands': createdBands.count(),
                'createdGenres': createdGenres.count(),
                'createdBandMembers': createdBandMembers.count()
            },
            'data': data
        }

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


class SimpleContributorSerializer(serializers.ModelSerializer):
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
