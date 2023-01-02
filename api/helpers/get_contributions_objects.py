import operator

from django.db.models import Count

from api.components.album.models import Album
from api.components.author.models import Artist, Band, BandMember
from api.components.genre.models import Genre
from api.components.track.models import Track


def get_contributions_objects(user):
    created_albums = Album.objects.filter(
        created_by=user).values('id', 'title', 'slug', 'release_type', 'artist__name', 'artist__slug', 'band__name',
                                'band__slug', 'created_at')

    created_tracks = Track.objects.filter(
        created_by=user).values('created_at', 'album__title', 'album__slug').annotate(tracks_count=Count('id'))

    # Needed because tracks are grouped in serializer
    created_tracks_count = Track.objects.filter(created_by=user).count()

    created_artists = Artist.objects.filter(
        created_by=user).values('id', 'name', 'slug', 'created_at')

    created_bands = Band.objects.filter(
        created_by=user).values('id', 'name', 'slug', 'created_at')

    created_genres = Genre.objects \
        .filter(created_by=user).filter(album_genres__isnull=False) \
        .values('created_at', 'album_genres__title', 'album_genres__slug').annotate(genres_count=Count('id'))

    created_genres_count = Genre.objects.filter(
        created_by=user).filter(album_genres__isnull=False).count()

    created_band_members = BandMember.objects.filter(
        created_by=user).values('id', 'artist__name', 'artist__slug', 'name', 'band__name', 'band__slug', 'created_at')

    for album in created_albums:
        album['type'] = 'Album'

    for track in created_tracks:
        track['type'] = 'Track'

    for artist in created_artists:
        artist['type'] = 'Artist'

    for band in created_bands:
        band['type'] = 'Band'

    for genre in created_genres:
        genre['type'] = 'Genre'

    for bandMember in created_band_members:
        bandMember['type'] = 'BandMember'

    data = list(created_albums) + list(created_tracks) + list(created_artists) + \
           list(created_bands) + list(created_genres) + list(created_band_members)

    data.sort(key=operator.itemgetter('created_at'), reverse=True)

    total = created_albums.count() + created_tracks_count + created_artists.count() + \
            created_bands.count() + created_genres.count() + created_band_members.count()

    # Points value:
    # Articles: 5 points
    # Albums, Bands, Artists: 3 points
    # Tracks, Genres, Band members, Edits: 1 point
    points = (created_albums.count() * 3) + created_tracks_count + (created_artists.count() * 3) + \
             (created_bands.count() * 3) + created_genres_count + \
             created_band_members.count()

    return {
        'counts': {
            'created_albums': created_albums.count(),
            'created_tracks': created_tracks_count,
            'created_artists': created_artists.count(),
            'created_bands': created_bands.count(),
            'created_genres': created_genres_count,
            'created_band_members': created_band_members.count(),
            'total': total,
            'points': points
        },
        'data': data
    }
