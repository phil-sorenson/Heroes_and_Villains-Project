from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail)
]