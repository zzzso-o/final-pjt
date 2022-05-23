from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [

    # 인기 영화 조회
    path('popularmovies/', views.popular_movies, name='popular_movies'),
    # 인기 영화 상세페이지
    path('popularmovies/<int:movies_pk>/', views.movie_detail, name='movie_detail'),
    
    # 영화 평점 조회
    # POST / movies/1/comments/ => 1번 영화에 평점달기
    # GET / movies/1/comments/ => 1번 영화의 모든 평점
    path('<int:movie_pk>/comments/', views.movie_comment_create),

    # PUT / movies/1/comments/1/ => 1번 영화에 달린 1번 평점 수정
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.movie_comment_update_delete),

]