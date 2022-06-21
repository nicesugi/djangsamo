from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleView.as_view()),
    # path('comment/', views.CommentView.as_view()),
]