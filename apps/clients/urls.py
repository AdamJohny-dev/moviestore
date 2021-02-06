from django.urls import path

from . import views


urlpatterns = [
    path('signup_client', views.signup, name='signup_client'),
    path('login_client', views.login, name='login_client'),
    path('logout_client', views.logout, name='logout_client'),
    path('dashboard_client', views.dashboard, name='dashboard_client'),
] 