from django.urls import path

from . import views


urlpatterns = [
    path('', views.account, name='userList'),
    path('users/<int:pk>/', views.user_details, name='userDetails'),
    path('list/', views.account, name="userList"),
]

