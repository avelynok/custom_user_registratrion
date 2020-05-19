from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.index, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview')
    
]