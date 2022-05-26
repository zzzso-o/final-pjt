from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display= ['name']

class MovieAdmin(admin.ModelAdmin):
    list_display= ['title', 'original_language','overview', 'release_date', 'poster_path', 'vote_average']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
