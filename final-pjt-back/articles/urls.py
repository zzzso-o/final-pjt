from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.article_index_create),
    path('<int:article_pk>/', views.article_detail_update_delete),
    path('<int:article_pk>/like/', views.like_article),

    # POST / articles/1/comments/ => 1번글에 댓글달기
    # GET / articles/1/comments/ = > 1번 글의 모든댓글

    path('<int:article_pk>/comments/', views.comment_create),
    # PUT / articles/1/commments/1/ => 1번 글에 달린 1번 댓글 수정
    # DELETE / articles/1/comments/1/ => 1번 글에 달린 1번 댓글 삭제
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_delete),
]
