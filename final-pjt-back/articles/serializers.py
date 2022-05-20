from rest_framework import serializers
from .models import Article, ArticleComment


# Article C/R(1)/U
class ArticleSerializer(serializers.ModelSerializer):
    # Comment R(all)
    class CommentListSerializer(serializers.ModelSerializer):

        class Meta:
            model = ArticleComment
            fields = ('id', 'content',)
    
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    comments = CommentListSerializer(many=True, read_only=True)


    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comments', 'created_at', 'updated_at')
        read_only_fields = ('comments',)
        

# Article R(all)
class ArticleListSerializer(serializers.ModelSerializer):

    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'comment_count')

# Comment C/U
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleComment
        fields = ('id','content', 'article',)
        read_only_fields = ('article',)