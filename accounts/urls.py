from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signin/', views.SIGNIN, name='signin'),
    path('signout/', views.SIGNOUT, name='signout'),
    path('signup/', views.SIGNUP, name='signup'),
]
