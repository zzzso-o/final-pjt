from django.contrib import admin
from .models import Movie, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display= ['pk', 'title']


class CommentAdmin(admin.ModelAdmin):
  list_display = ['pk', 'content']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)
