from django.shortcuts import render
from apps.moviestore.models import Movie
from apps.owners.models import Owner
from apps.clients.models import Client

def search_by_genre(request):

    id = request.user.id

    client = Client.objects.filter(user=id)
    owner= Owner.objects.filter(user=id)
    if client.exists():
        right_user = Client.objects.get(user=id)
    elif owner.exists():
        right_user = Owner.objects.get(user=id)
    else:
        right_user=""


    
    movies_list = Movie.objects.order_by('title')
    

    if 'list-genres' in request.GET:
        search_genre = request.GET['list-genres']
        movies_list = movies_list.filter(genre__icontains=search_genre).filter(quantity_stock__gte=0)

    data = {
        'movies': movies_list,
        'right_user': right_user
    }


    return render(request, 'movies/search_genre.html', data)