from rest_framework import serializers
from .models import Movie, MovieComment

# 전체 영화 조회(GET)
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_user', 'movie_likes')

# 상세 영화 조회 (GET)
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_user', 'movie_likes')


# 상세 영화 전체 평점 조회(GET)
class CommentSerializer(serializers.ModelSerializer):
    comment_title = serializers.SerializerMethodField()
    def get_comment_title(self, obj):
        return obj.comment.title
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username
    class Meta:
        model = MovieComment
        fields = ('id', 'userName', 'user', 'comment', 'comment_content', 'created_at',)
        read_only_fields = ('user','comment',)
