from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article, ArticleComment

User = get_user_model()



# class ArticleSerializer(serializers.ModelSerializer):
    
#     class CommentListSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = ArticleComment
#             fields = ('id', 'article_comment_content',)
    
#     article_title = serializers.CharField(min_length=2, max_length=100)
#     article_content = serializers.CharField(min_length=2)
#     comments = CommentListSerializer(many=True, read_only=True)
#     user = UserSerializer(read_only=True)


#     class Meta:
#         model = Article
#         fields = ('id', 'article_title', 'article_content', 'comments', 'article_created_at', 'article_updated_at',)
#         read_only_fields = ('comments', 'article_created_at', 'article_updated_at',)
# 
# class ArticleSerializer(serializers.ModelSerializer):
    

# class CommentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = ArticleComment
#         fields = ('id','article_comment_content', 'article',)
#         read_only_fields = ('article',)
class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = ArticleComment
        fields = ('pk', 'user', 'article_comment_content', 'article', 'article_comment_created_at', 'article_comment_updated_at')
        read_only_fields = ('article', 'article_comment_created_at', 'article_comment_updated_at')



class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    article_comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    article_likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'article_title', 'article_content', 'article_comments', 'article_likes')

   


# class ArticleListSerializer(serializers.ModelSerializer):

#     comment_count = serializers.IntegerField(source='comments.count', read_only=True)
#     like_count = serializers.IntegerField()

#     class Meta:
#         model = Article
#         fields = ('id', 'article_title', 'comment_count')

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


