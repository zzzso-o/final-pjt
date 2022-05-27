
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie, MovieComment



class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'article_title', 'article_content')

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields =('pk', 'title' , 'comments' , 'genres')

    class MovieCommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = MovieComment
            fields = ('pk', 'movie', )

    article_likes = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    like_users = MovieSerializer(many=True)
    comment_user = MovieCommentSerializer(many=True)



    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'article_likes', 'articles', 'like_users', 'comment_user', )
