from django.urls import path

from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('<int:movie_id>', movie, name='movie'),
    path('search_by_title', search_by_title, name='search'),
    path('search_by_genre', search_by_genre, name='search_genre'),
    path('create/movie', create_movie, name='create_movie'),
    path('delete/<int:movie_id>', delete_movie, name='delete_movie'),
    path('edit/<int:movie_id>', edit_movie, name='edit_movie'),
    path('update_movie', update_movie, name="update_movie"),
] 