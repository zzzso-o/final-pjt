from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    article_created_at = models.DateTimeField(auto_now_add=True)
    article_updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
