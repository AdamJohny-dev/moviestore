from django.shortcuts import render, redirect, get_object_or_404
from apps.clients.models import Client
from apps.moviestore.models import Movie
from .models import Rent
from django.contrib.auth.models import User
from django.contrib import messages
from django.core import serializers
import ctypes




def rent(request):

    """ Create new rent of a movie previously chosen by client """

    if request.method == 'POST':
        name = request.POST['name']
        movie_name = request.POST['movie-name']
        cpf = request.POST['cpf']
        date_start = request.POST['date-start']
        date_end = request.POST['date-end']

        if verify_data(date_start, date_end):
            messages.error(request, 'End date should be greater than start date.')
            return redirect('rent_movie')

        movie = Movie.objects.get(title=movie_name)

        movie.quantity_stock = decrease_stock(movie.quantity_stock)
        movie.save()
        
        client = Client.objects.get(name=name)
        rent = Rent.objects.create(client=client, movie_name=movie_name, cpf=cpf,
            date_start=date_start, date_end=date_end)
        rent.save()
        return redirect('dashboard_client')
    else:
        return redirect('index')

def details(request):

    """ Show the details of rented movie """

    if request.method == 'POST':
        return redirect('dashboard_client')
    else:
        return redirect('index')

def cancel(request): 

    """ Cancel a rented movie (it disappears of dashboard client) """

    if request.method == 'POST':

        movie_name = request.POST['movie-name']
        movie_name_taken = request.POST['movie-name-taken']
        print(movie_name)
        print(movie_name_taken)
        

        if empty_field(movie_name):
            
            messages.error('Warning', 'The field cannot be blank!')
            print("Blank Field")
            return redirect('dashboard_client')

        if wrong_typed_movie(movie_name, movie_name_taken):
            
            messages.error(request, 'The name of movie is wrong!')
            print("Wrong movie")
            return redirect('dashboard_client')
        
        print('Aqui: '+ movie_name_taken)
        
        id = request.user.id
        user = User.objects.get(id=id)
        client = Client.objects.get(user=user)
        rent = Rent.objects.all().filter(client=client, movie_name=movie_name)

        
        rent_to_delete = Rent.objects.get(id=rent[0].pk)
        rent_to_delete.delete()

        movie = Movie.objects.get(title=movie_name)
        movie.quantity_stock = increase_stock(movie.quantity_stock)
        movie.save()

        print("Aqui:",rent_to_delete.id)
        
        return redirect('dashboard_client')
    else:
        return redirect('index')
   
def verify_data(date_start, date_end ):

    """ Verify if the dates are correct """

    return date_start > date_end

def decrease_stock(quantity_stock):

    """ Represents the action of rent a movie """

    return quantity_stock - 1

def increase_stock(quantity_stock):

    """ Represents the action of cancel the rent contract """

    return quantity_stock + 1

def empty_field(field):
    """ Avoid empty fields  """

    return not field.strip()

def wrong_typed_movie(movie_name, movie_name_taken):

    """ Avoid the wrong typed movie on cancel window """

    return movie_name != movie_name_taken