from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/send-alert/', views.send_alert, name='send_alert'),
    path('api/book/', views.book_helper, name='book_helper'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]