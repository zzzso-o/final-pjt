from rest_framework import serializers
from .models import Article, ArticleComment



class ArticleSerializer(serializers.ModelSerializer):
    
    class CommentListSerializer(serializers.ModelSerializer):

        class Meta:
            model = ArticleComment
            fields = ('id', 'article_comment_content',)
    
    article_title = serializers.CharField(min_length=2, max_length=100)
    article_content = serializers.CharField(min_length=2)
    comments = CommentListSerializer(many=True, read_only=True)
    user_id = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'article_title', 'article_content', 'comments', 'article_created_at', 'article_updated_at', 'user_id')
        read_only_fields = ('comments', 'article_created_at', 'article_updated_at')
        


class ArticleListSerializer(serializers.ModelSerializer):

    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'article_title', 'comment_count')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleComment
        fields = ('id','article_comment_content', 'article',)
        read_only_fields = ('article',)