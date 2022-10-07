import operator
from django.db.models import Count
from rest_framework import serializers

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
            created_by=obj.user).values('id', 'title', 'slug', 'release_type', 'artist__name', 'artist__slug', 'band__name', 'band__slug', 'created_at')

        createdTracks = Track.objects.filter(
            created_by=obj.user).values('created_at', 'album__title', 'album__slug').annotate(tracks_count=Count('id'))

        # Needed because tracks are grouped in serializer
        createdTracksCount = Track.objects.filter(created_by=obj.user).count()

        createdArtists = Artist.objects.filter(
            created_by=obj.user).values('id', 'name', 'slug', 'created_at')

        createdBands = Band.objects.filter(
            created_by=obj.user).values('id', 'name', 'slug', 'created_at')

        createdGenres = Genre.objects\
            .filter(created_by=obj.user).filter(album_genres__isnull=False)\
            .values('created_at', 'album_genres__title', 'album_genres__slug').annotate(genres_count=Count('id'))

        createdGenresCount = Genre.objects.filter(
            created_by=obj.user).filter(album_genres__isnull=False).count()

        createdBandMembers = BandMember.objects.filter(
            created_by=obj.user).values('id', 'artist__name', 'artist__slug', 'name', 'band__name', 'band__slug', 'created_at')

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

        total = createdAlbums.count() + createdTracksCount + createdArtists.count() + \
            createdBands.count() + createdGenres.count() + createdBandMembers.count()

        # Points value:
        # Articles: 5 points
        # Albums, Bands, Artists: 3 points
        # Tracks, Genres, Band members, Edits: 1 point
        points = (createdAlbums.count() * 3) + createdTracksCount + (createdArtists.count() * 3) + \
            (createdBands.count() * 3) + createdGenresCount + \
            createdBandMembers.count()

        return {
            'counts': {
                'createdAlbums': createdAlbums.count(),
                'createdTracks': createdTracksCount,
                'createdArtists': createdArtists.count(),
                'createdBands': createdBands.count(),
                'createdGenres': createdGenresCount,
                'createdBandMembers': createdBandMembers.count(),
                'total': total,
                'points': points
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
        lookup_field = 'user'
        extra_kwargs = {
            'url': {'lookup_field': 'user'},
        }


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
