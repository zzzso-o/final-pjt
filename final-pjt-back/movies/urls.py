from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [

    # 인기 영화 조회
    path('popularmovies/', views.popular_movies, name='popular_movies'),
    # 인기 영화 상세페이지
    path('popularmovies/<int:movies_pk>/', views.movie_detail, name='movie_detail'),
    # 영화 평점 조회
    path('<int:movie_pk>/comments/', views.movie_comments, name='movie_comments'),

]