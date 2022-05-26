from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=100)
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies')

    # like : movie M:N 외래키

    # def __str__(self):
    #     return self.movie_title

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    # user : comment 1:N 외래키
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    # movie : comment 1:N 외래키
   
    movie_comment_content = models.CharField(max_length=100)
    movie_comment_created_at = models.DateTimeField(auto_now_add=True)
    movie_comment_updated_at = models.DateTimeField(auto_now=True)

    # 유저평점
    user_score = models.FloatField()

    # def __str__(self):
    #     return self.movie_comment_content

    #  user X 
    #  movie 여러개 X
    #  Comment 1개 ?

