from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework import status

from user.serializers import UserSerializer
from Django.permissions import IsAdminOrIsAuthenticatedReadOnly
from user.models import User as UserModel


# 127.0.0.1:8000/user/
class UserView(APIView):
    
    # 사용자 조회
    def get(self, request):
        permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
        user_serializer = UserSerializer(request.user, context={"request": request}).data
        return Response(user_serializer, status=status.HTTP_200_OK)
    
    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data, context={"request": request})
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 회원정보 수정
    def put(self, request, obj_id):
        user = UserModel.objects.get(id=obj_id)
        user_serializer = UserSerializer(user, data=request.data, partial=True, context={"request": request})
        ## 비밀번호 수정
        # if password == check_password:
        #     pass
        # else:
        #     error : 입력한 패스워드가 일치하지 않습니다.
            
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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



