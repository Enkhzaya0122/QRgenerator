from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('forgot1/', views.forgot1),
    path('forgot2/', views.forgot2),
    path('forgot3/', views.forgot3),
]
