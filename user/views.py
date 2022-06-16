from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
class UserView(APIView):
    # 로그인
    def post(self, request):

        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP.status)

        login(request, user)
        print(f'{request.data} 의 user {user}')
        return Response({"message": "로그인 성공!!"})

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message":"로그아웃 성공"})



