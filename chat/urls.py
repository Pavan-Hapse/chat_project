# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('signup/', views.signup, name='signup'),  # Add this line for signup
    path('login/', views.login_view, name='login'),


]