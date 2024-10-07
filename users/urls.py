from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_list, name='list'),
    path('register/', views.register, name='register'),
]
