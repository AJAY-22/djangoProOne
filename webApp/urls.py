from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('users/<int:pk>/', views.user_details, name='userDetails'),
]
