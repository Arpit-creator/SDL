from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HOME, name='home'),
    path('user/', views.USER, name='user'),
]
