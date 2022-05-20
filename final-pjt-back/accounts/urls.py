from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


app_name = 'accounts'

urlpatterns = [
    
    path('api-token-auth/', obtain_jwt_token),
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),


]
