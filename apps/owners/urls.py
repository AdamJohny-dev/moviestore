from django.urls import path

from . import views


urlpatterns = [
    path('signup_owner', views.signup, name='signup_owner'),
    path('login_owner', views.login, name='login_owner'),
    path('logout_owner', views.logout, name='logout_owner'),
    path('dashboard_owner', views.dashboard, name='dashboard_owner'),
] 