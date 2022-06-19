from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework import status

from user.serializers import UserSerializer


# 127.0.0.1:8000/user/
class UserView(APIView):
    # permission_classes = [permissions.AllowAny]
    # 사용자 조회
    def get(self, request):
        user=request.user
        return Response(UserSerializer(user).data)
    
    # 회원가입
    def post(self, request):
        return Response({"msssage":"회원가입"})
    
    # 회원정보 수정
    def put(self, request):
        return Response({"msssage":"회원정보 수정"})
    
    # 회원탈퇴
    def delete(self, request):
        return Response({"message":"회원탈퇴"})
    
    
    
    
# 127.0.0.1:8000/user/login/
class UserAPIView(APIView):    
    # 로그인
    def post(self, request):

        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        print(f'{request.data} 로그인 성공') 
        return Response({"message": "로그인 성공!!"})

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message":"로그아웃 성공"})



