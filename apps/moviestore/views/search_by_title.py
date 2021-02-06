from django.shortcuts import render
from apps.moviestore.models import Movie
from apps.owners.models import Owner
from apps.clients.models import Client

def search_by_title(request):

    id = request.user.id

    client = Client.objects.filter(user=id)
    owner= Owner.objects.filter(user=id)
    if client.exists():
        right_user = Client.objects.get(user=id)
    elif owner.exists():
        right_user = Owner.objects.get(user=id)
    else:
        right_user=""


    movies_list = Movie.objects.order_by('title').filter(quantity_stock__gte=0)

    if 'search' in request.GET:
        search_title = request.GET['search']
        movies_list = movies_list.filter(title__icontains=search_title)

    data = {
        'movies': movies_list,
        'right_user': right_user
    }


    return render(request, 'movies/search.html', data)