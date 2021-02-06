from django.shortcuts import redirect, render, get_object_or_404
from apps.moviestore.models import Movie
from apps.rented.models import Rent
from apps.clients.models import Client
from apps.owners.models import Owner
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    """ Root of all apps """

    id = request.user.id

    client = Client.objects.filter(user=id)
    owner= Owner.objects.filter(user=id)
    if client.exists():
        right_user = Client.objects.get(user=id)
    elif owner.exists():
        right_user = Owner.objects.get(user=id)
    else:
        right_user=""

    movies = Movie.objects.order_by('title').filter(quantity_stock__gte=0)
    paginator = Paginator(movies, 3)
    page = request.GET.get('page')
    movies_by_page = paginator.get_page(page)

    data = {
        'movies': movies_by_page,
        'right_user': right_user
    }

    return render(request, 'movies/index.html', data)

def movie(request, movie_id):

    """ Build the page movie """

    id = request.user.id

    client = Client.objects.filter(user=id)
    owner= Owner.objects.filter(user=id)
    if client.exists():
        right_user = Client.objects.get(user=id)
    elif owner.exists():
        right_user = Owner.objects.get(user=id)
    else:
        right_user=""

    movie = get_object_or_404(Movie, pk=movie_id)

    movie_to_show = {
        'movie': movie,
        'right_user': right_user
    }
   

    return render(request, 'movies/movie.html', movie_to_show)

def create_movie(request):

    """ Create a new movie based on data typed by owner """

    if request.method == 'POST':
        title = request.POST['title']
        year = request.POST['year']
        director = request.POST['director']
        genre = request.POST['genre']
        description = request.POST['description']
        picture = request.FILES['picture']
        imdb_score = request.POST['imdb_score']
        price = request.POST['price']
        quantity_stock = request.POST['stock']
        
        user = get_object_or_404(User, pk=request.user.id)
        movie = Movie.objects.create(user=user, title=title, year=year, director=director, 
                    genre=genre, description=description, picture=picture, imdb_score=imdb_score,
                    quantity_stock=quantity_stock, price=price)
        movie.save()
        return redirect('dashboard_owner')
    else:
        return render(request, 'movies/create_movie.html')

def edit_movie(request, movie_id):

    """ Edit a movie based on id of auth user (owner) """

    id = request.user.id
    movie = get_object_or_404(Movie, pk=movie_id)
    user = User.objects.get(id=id)
    owner = Owner.objects.get(user=user)
    updated_movie = {
        'movie': movie,
        'owner': owner
    }
    
    return render(request, 'movies/edit_movie.html', updated_movie)

def delete_movie(request, movie_id): 

    """ Delete a movie chosed by owner """

    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('dashboard_owner')

def update_movie(request):

    """ Update a movie based on data typed by the owner """

    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        updated_movie = Movie.objects.get(pk=movie_id)

        updated_movie.title = request.POST['title']
        updated_movie.year = request.POST['year']
        updated_movie.director = request.POST['director']
        updated_movie.genre = request.POST['genre']
        updated_movie.description = request.POST['description']
        if 'picture' in request.FILES:
            updated_movie.picture = request.FILES['picture']
        updated_movie.imdb_score = request.POST['imdb_score']
        updated_movie.price = request.POST['price']
        updated_movie.quantity_stock = request.POST['stock']

        updated_movie.save()
        return redirect('dashboard_owner')