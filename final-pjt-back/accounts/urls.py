from django.urls import path
from . import views
from rest_framework import urls

app_name = 'accounts'

urlpatterns = [
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),

    # 나의 프로필
    path('<username>/', views.profile, name='profile'),
    # 나의 작성글 목록
    path('<username>/articles/', views.profile_articles, name='profile_articles'),
    # 나의 작성댓글
    path('<username>/articles/comments/', views.profile_articles_comments, name='profile_articles_comments'),
    # 나의 찜한 영화 목록
    path('<username>/likemovies/', views.profile_like_movies, name='profile_like_movies'),

]
