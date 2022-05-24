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


# 영화 평점 생성(POST)
@api_view(['POST',])
def movie_comment_create(request, article_pk):
    movie = get_object_or_404(Movie, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)


# 영화 평점 수정, 삭제(PUT, DELETE)
@api_view(['PUT', 'DELETE',])
def movie_comment_update_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    def movie_comment_update():
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def movie_comment_delete():
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        return movie_comment_update()
    elif request.method == 'DELETE':
        return movie_comment_delete()