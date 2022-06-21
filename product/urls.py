from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductView.as_view()),
    path('<obj_id>/', views.ProductView.as_view()),
]