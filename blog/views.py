import datetime
from sre_constants import CATEGORY_SPACE
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from .models import Comment
from user.models import User
from user.serializers import ArticleSerializer, UserSerializer
from Django.permissions import RegistedMoreThanThreeDaysUser
from Django.permissions import IsAdminOrIsAuthenticatedReadOnly
from user.serializers import ArticleSerializer
from datetime import datetime

class ArticleView(APIView):
    # 게시글 조회
    # def get(self, request):
    #     user=request.user

    #     return Response(UserSerializer(user).data) 
    def get(self, request):
        permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
        today = datetime.now()
        articles = ArticleModel.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
        ).order_by("-id")
        
        return Response(ArticleSerializer(articles, many=True).data, status=status.HTTP_200_OK)
    
    # 게시글 작성 (3일 이상 지난 사용자만 게시글 작성 가능)
    def post(self, request):
        permission_classes = [RegistedMoreThanThreeDaysUser]
        user = request.user
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        categorys = request.data.pop('category', [])
        
        if len(title) <= 5:
            return Response({"error": "타이틀은 5자 이상 작성해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        if len(content) <= 20:
            return Response({"error": "내용은 20자 이상 작성해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        if not categorys:
            return Response({"error": "카테고리가 지정되지 않았습니다"}, status=status.HTTP_400_BAD_REQUEST)
        article = ArticleModel(
            user=user,
            **request.data
        )
        article.save()
        article.category.add(*categorys)
        return Response({"message": "성공"}, status=status.HTTP_200_OK)
        
        # author = request.user
        # title = request.data.get('title', '')
        # category = request.data.get('category', '')
        # content = request.data.get('content', '')
        
        # article, created = ArticleModel.objects.get_or_create(
        #     title = title,
        #     content = content,
        #     )     

        # if created:
        #     article.author = author
        #     article.category.add(category)
        #     article.title = title
        #     article.content = content
        #     article.save()
        #     return Response({"message": "게시글 작성 성공!!"}, status=status.HTTP_200_OK)
        
        # elif len(title) < 5 or len(content) < 20 or category =='':
        #     return Response({"message": "조건이 충족되지 않았습니다!!"}, status=status.HTTP_411_LENGTH_REQUIRED)
        # else:
        #     return Response({"message":"이미 작성된 글입니다"}, status=status.HTTP_400_BAD_REQUEST)



class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    # 댓글 조회
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)
    
    
    # 댓글 작성
    def post(self, request):
        return Response({"message":"comment view-post"})
        
