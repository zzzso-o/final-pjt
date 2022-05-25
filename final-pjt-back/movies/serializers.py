from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie, MovieComment

User = get_user_model()

# 전체 영화 조회
class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()


    class Meta:
        model = Movie
        fields = ('pk', 'title', 'like_count', 'comments_count')


# 상세 영화 조회
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_user', 'movie_likes')


# 상세 영화 전체 평점 조회
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = MovieComment
        fields = ('pk', 'user', 'movie_comment_content', 'movie', 'movie_comment_created_at', 'movie_comment_updated_at')
        read_only_fields = ('movie', 'movie_comment_created_at', 'movie_comment_updated_at')
