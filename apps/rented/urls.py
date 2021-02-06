from django.urls import path

from apps.rented import views



urlpatterns = [
    path('rent_movie', views.rent, name='rent_movie'),
    path('details', views.details, name='details_movie'),
    path('cancel', views.cancel, name='cancel_warning')
] 