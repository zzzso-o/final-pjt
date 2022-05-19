from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_language = models.CharField
    release_date = models.DateTimeField()
    poster_path = models.CharField(max_length=100)
    vote_average = models.FloatField()
    genre = models.CharField(max_length=50)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # like : movie M:N 외래키

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # user : comment 1:N 외래키
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # movie : comment 1:N 외래키
   
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 유저평점
    user_score = models.FloatField()

    def __str__(self):
        return self.content
