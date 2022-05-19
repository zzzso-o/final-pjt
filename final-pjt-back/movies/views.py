from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Comment

from django.contrib.auth import get_user_model


def home(requests):
    pass

def popular_movies(requests):
    pass

def movie_detail(requests):
    pass

def movie_comments(requests):
    pass