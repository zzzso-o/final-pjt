from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    article_title = models.CharField(max_length=50)
    article_content = models.TextField()
    article_created_at = models.DateTimeField(auto_now_add=True)
    article_updated_at = models.DateTimeField(auto_now=True)
    article_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_likes')


class ArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    article_comment_content = models.CharField(max_length=100)
    article_comment_created_at = models.DateTimeField(auto_now_add=True)
    article_comment_updated_at = models.DateTimeField(auto_now=True)
