from django.shortcuts import get_object_or_404, render
from django.db.models import Count

# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status

from .models import Article, ArticleComment
from .serializers import (
    ArticleSerializer, 
    ArticleListSerializer,
    CommentSerializer,
)


@api_view(['GET', 'POST'])
@login_required
# (login_url='/accounts/login')
def article_index_create(request):

    def article_index():
        # comment 개수 추가
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('article_likes', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    def article_create():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_index()
    elif request.method == 'POST':
        return article_create()



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def article_update():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)    
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def article_delete():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    
    if request.method == 'GET':
        return article_detail()
    if request.method == 'PUT':
        if request.user == article.user:
            return article_update()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return article_delete()


@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)



@api_view(['POST',])
def comment_create(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE',])
def comment_update_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(ArticleComment, pk=comment_pk)

    def comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()