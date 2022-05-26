from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie, MovieComment

User = get_user_model()

# 상세 영화 전체 평점 조회
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = MovieComment
        fields = ('pk', 'user', 'movie_comment_content', 'movie', 'movie_comment_created_at', 'movie_comment_updated_at', 'user_score')
        read_only_fields = ('movie',)

# 전체 영화 조회
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'release_date', 'poster_path')


# 상세 영화 조회
class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    # user_score_avg = serializers.FloatField()
    comments = CommentSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk','title', 'release_date', 'genres', 'overview', 'vote_average', 'like_users', 'poster_path', 'comments',)


