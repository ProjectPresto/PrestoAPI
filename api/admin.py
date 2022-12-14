from django.contrib import admin
from .components.album import models as album_models
from .components.author import models as author_models
from .components.track import models as track_models


@admin.register(album_models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'artist_id',
        'band_id',
        'release_date',
        'created_by',
        'updated_by'
    ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_per_page = 30
    ordering = ['title']
    search_fields = ['title']
    list_select_related = ['artist_id', 'band_id', 'created_by', 'updated_by']
    autocomplete_fields = ['artist_id', 'band_id', 'created_by', 'updated_by']


@admin.register(track_models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'album_id',
        'created_by',
        'updated_by'
    ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_per_page = 30
    ordering = ['title']
    search_fields = ['title']
    list_select_related = ['album_id', 'created_by', 'updated_by']
    autocomplete_fields = ['album_id', 'created_by', 'updated_by']


@admin.register(author_models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'birth_date',
        'death_date',
        'created_by',
        'updated_by'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    list_per_page = 30
    ordering = ['name']
    search_fields = ['name', 'created_by', 'updated_by']
    autocomplete_fields = ['created_by', 'updated_by']


@admin.register(author_models.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'founding_year',
        'breakup_year',
        'created_by',
        'updated_by'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    list_per_page = 30
    ordering = ['name']
    search_fields = ['name', 'created_by', 'updated_by']
    autocomplete_fields = ['created_by', 'updated_by']
