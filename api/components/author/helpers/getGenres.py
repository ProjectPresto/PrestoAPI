from api.components.album.models import Album
from api.components.genre.models import Genre


def get_genres(self, obj, obj_type):
    albums = Album.objects
    if obj_type == 'band':
        albums = albums.filter(band_id=obj.id)
    else:
        albums = albums.filter(artist_id=obj.id)

    genres = {}
    for a in albums:
        album_genres = Genre.objects.filter(album_genres=a.id)
        for g in album_genres:
            if (g.name in genres):
                genres[g.name] += 1
            else:
                genres[g.name] = 1

    genres = dict(
        sorted(genres.items(), key=lambda item: item[1], reverse=True))
    return [g for g in genres]
