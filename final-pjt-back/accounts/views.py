from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    # Client에서 온 데이터를 받기
    if password != password_confirmation:
    # 패스워드 일치 여부 체크
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    
    # UserSerializer를 통해 데이터 직렬화
    if serializer.is_valid(raise_exception=True):
    # 유효성 검사(비밀번호도 직렬화)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        # 비밀번호 해싱
        user.save()
        # password는 직렬화되어도 response에서 표현되지 않는다
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)
