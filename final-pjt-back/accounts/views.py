from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import UserSerializer


def signup(requests):
    pass

def login(requests):
    pass

def logout(reuqests):
    pass

def profile(reuqests):
    pass

def profile_articles(requests):
    pass

def profile_articles_comments(requests):
    pass

def profile_like_movies(requests):
    pass