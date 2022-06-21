from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('', views.UserView.as_view()),
    path('<obj_id>/', views.UserAPIView.as_view()),
]