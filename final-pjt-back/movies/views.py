from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, MovieComment
from .serializers import MovieSerializer, MovieListSerializer, CommentSerializer

from django.contrib.auth import get_user_model


# 인기영화 리스트 조회(GET)
@api_view(['GET'])
def popular_movies(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

# 인기영화 상세 조회(GET)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# 영화 평점 생성(POST)
@api_view(['POST',])
def movie_comment_create(request, movie_pk,):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    serializer = CommentSerializer(data=request.data)

    # if comments.filter(user_id=user.pk).exists(): # 이미 댓글을 남긴 사용자라면
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    # else:
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 영화 평점 수정, 삭제(PUT, DELETE)
@api_view(['PUT', 'DELETE',])
def movie_comment_update_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    def movie_comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def movie_comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return movie_comment_update()
    elif request.method == 'DELETE':
        return movie_comment_delete()