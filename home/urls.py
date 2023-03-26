from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home.home'),
    path('login', views.LoginInterfaceView.as_view(), name = 'home.login'),
    path('logout', views.LogoutInterfaceView.as_view(), name = 'home.logout'),
    path('register', views.SignUpView.as_view(), name= 'home.register')
]
