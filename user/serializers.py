from dataclasses import field
from xml.etree.ElementTree import Comment
from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

class ArticleSerializer(serializers.ModelSerializer):
    articles_user = serializers.SerializerMethodField()
    def get_articles_user(self, obj):
        return obj.author.fullname

    class Meta:
        model = ArticleModel
        fields = ["title", "category", "content", "articles_user"]


class CommentSerializer(serializers.ModelSerializer):
    comments_user = serializers.SerializerMethodField()
    def get_comments_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = CommentModel
        fields = ["article", "content", "comments_user"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age"]
        
        
class UserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    userprofile = UserProfileSerializer() 
    
    class Meta:
        model = UserModel
        fields = [
            "id", "last_login", "username", "email", 
            "userprofile", "article_set", "comment_set"
        ]