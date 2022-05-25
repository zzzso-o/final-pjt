from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article, ArticleComment

User = get_user_model()



class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = ArticleComment
        fields = ('pk', 'user', 'article_comment_content', 'article','article_comment_created_at','article_comment_updated_at')
        read_only_fields = ('article', )



class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')


    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    article_likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'article_title', 'article_content', 'comments', 'article_likes', 'article_created_at', 'article_updated_at')

   


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'article_title', 'comment_count', 'like_count')


