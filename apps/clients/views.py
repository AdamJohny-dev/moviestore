from django import template
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth, messages
from apps.moviestore.models import Movie
from apps.rented.models import Rent
from django.contrib.auth.models import User
from .models import Client
from django.http import request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def signup(request):

    """ Register a new client  """

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        cpf = request.POST['cpf']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if empty_field(name):
            messages.error(request, 'The field name is required!')
            return render(request, 'clients/signup_client.html', status=400)

        if empty_field(email):
            messages.error(request, 'The field email is required!')
            return render(request, 'clients/signup_client.html', status=400)

        if len(password) < 4:
            messages.error(request, 'The password needs at leats 5 caracteres!')
            return render(request, 'clients/signup_client.html', status=400)

        if passwords_not_match(password, password2):
            messages.error(request, 'The passwords dont match')
            return render(request, 'clients/signup_client.html', status=400)

        if empty_field(cpf):
            messages.error(request, 'The field cpf is required!')
            return render(request, 'clients/signup_client.html', status=400)

        if  Client.objects.filter(email=email).exists():
            messages.error(request, 'User already taken')
            return render(request, 'clients/signup_client.html', status=400)

        if Client.objects.filter(name=name).exists():
            messages.error(request, 'User already taken')
            return render(request, 'clients/signup_client.html', status=400)

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
       
        client = Client.objects.create(user=user, name=user.username, email=user.email, cpf=cpf)
        messages.success(request, 'Client successfully registered!')

        return redirect('login_client')
    else:
        return render(request, 'clients/signup_client.html')

def login(request):

    """ Allows clients to login  """

    
    if request.method == 'POST':
        email = request.POST['email']
        if empty_field(email):
            messages.error(request, 'The field email cant be blank!')
            return render(request, 'clients/login_client.html', status=401)

        password = request.POST['password']
        if empty_field(email) or empty_field(password):
            messages.error(request, 'The fields email and password cant be blank!')
            return render(request, 'clients/login_client.html', status=401)

        if Client.objects.filter(email=email).exists() and User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password )
            if user is not None: 
                auth.login(request, user)
                return redirect('dashboard_client')
            else:
                messages.error(request, 'Email or password is invalid!')
                return redirect('login_client')
        else:
            messages.error(request, 'Client account not exists! ')
            return redirect('login_client')
    
    return render(request, 'clients/login_client.html')

def logout(request):

    """ Allows users to logout  """

    auth.logout(request)
    return redirect('index')

def dashboard(request):

    """ Opens the area of logged user  """

    if request.user.is_authenticated:
        id = request.user.id
        
        user = User.objects.get(id=id)
        client = Client.objects.get(user=user)
        rent = Rent.objects.all().filter(client=client)
        object_rents = []
        object_movies = []

        for i in range(0, len(rent)):
            rented_movie = Movie.objects.get(title=rent[i].movie_name)
            rented_movie.available = False
            rented_movie.save()
            object_movies.append(rented_movie)
        
        
        paginator = Paginator(object_movies, 3)
        page = request.GET.get('page')
        movies_by_page = paginator.get_page(page)

        data = {
            'movies': movies_by_page,
            'rents':  rent
        }
        return render(request, 'clients/dashboard_client.html', data)
        
    else:
        return redirect('index')



def empty_field(field):

    """ Avoid empty fields  """

    return not field.strip()

def passwords_not_match(password, password2):
    
    """ Avoid wrong match of passwords on signup_client window  """

    return password != password2


