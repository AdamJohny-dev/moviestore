from django.contrib import admin
from .models import Movie


class MoviesList(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'year', 'available')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('genre',)
    list_editable = ('available',)
    list_per_page = 2

admin.site.register(Movie, MoviesList) 

