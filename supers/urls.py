from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.supers_list),
    # path('', views.supes_list),
    # path('<int:pk>/', views.products_detail)
]