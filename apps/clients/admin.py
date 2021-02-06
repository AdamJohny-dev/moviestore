from django.contrib import admin
from .models import Client
from django.contrib.auth.models import User


class ClientList(admin.ModelAdmin):
    list_display = ('id','user','cpf')
    list_display_links = ('id', 'user',)
    search_fields = ('user',)
    list_per_page = 2

admin.site.register(Client, ClientList)
