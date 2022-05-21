from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display= ['genre_name']

class MovieAdmin(admin.ModelAdmin):
    list_display= ['movie_title', 'original_language', 'release_date', 'poster_path', 'vote_average', 'movie_likes']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
