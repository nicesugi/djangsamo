from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone


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
