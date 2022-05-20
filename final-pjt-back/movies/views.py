from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, MovieComment
from .serializers import MovieSerializer, MovieListSerializer, CommentSerializer

from django.contrib.auth import get_user_model


# 인기영화 리스트 조회(GET)
@api_view(['GET'])
def popular_movies(requests):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

# 인기영화 상세 조회(GET)
@api_view(['GET'])
def movie_detail(requests, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화 평점 조회
def movie_comments(requests):
    pass

