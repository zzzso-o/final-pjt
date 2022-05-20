
from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
# from movies.models import Movie


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # write_only : 시리얼라이징은 하지만 응답에는 포함시키지 않음
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )


class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')


    # class MovieSerializer(serializers.ModelSerializer):

    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title')

    # articles = ArticleSerializer(many=True)
    # article_comments = ArticleSerializer(many=True)

    # like_movies = MovieSerializer(many=True)
    # movie_comments = MovieSerializer(many=True)

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'password', 'first_name', 'last_name', 'articles', 'article_comments', 'like_movies', 'movie_comments')
    #     read_only_fields = ('movie_commnets', 'like_movies', 'article_comments', 'articles')