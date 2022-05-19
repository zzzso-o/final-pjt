from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'articles', 'article_comments', 'like_movies', 'movie_comments')
        read_only_fields = ('movie_commnets', 'like_movies', 'article_comments', 'articles')