from django.db import models
from django.conf import settings


class Article(models.Model):
    article_title = models.CharField(max_length=50)
    ariticle_content = models.TextField()
    article_created_at = models.DateTimeField(auto_now_add=True)
    article_updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_likes')

    # def __str__(self):
    #     return self.article_title


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_comment_content = models.CharField(max_length=100)
    article_comment_created_at = models.DateTimeField(auto_now_add=True)
    article_comment_updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.article_comment_content
