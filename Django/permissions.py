from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status


class RegistedMoreThanThreeDaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """
    
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        # Date field : 2020-10-2join_date.strftime("%Y-%m-%d"))
        # DateTime field : 2020-10-2 10:20:32
        join_date = user.join_date
        three_days_ago = timezone.now() - timedelta(days=3)
        print(f'가입한 날짜 = {join_date}')
        print(f'지금 날짜 = {timezone.now()}')
        print(f'3일 전 = {three_days_ago}')

        return bool(join_date < three_days_ago)


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)


class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        # 로그인 사용자가 get 요청 시 True
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        # admin 사용자이거나 가입일이 7일 이상 된 사용자의 경우 True
        if user.is_authenticated and user.is_admin or \
            user.join_date < (datetime.now().date() - timedelta(days=7)):
            return True
            
        return False