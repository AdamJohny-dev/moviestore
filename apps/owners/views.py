from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth, messages
from apps.moviestore.models import Movie
from django.contrib.auth.models import User
from .models import Owner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def signup(request):

    """ Register a new owner  """

    serialkeyCustom = "g\C_%8=5*;?z:6J+@uW_4+3_nj3r=?qY_6HG!%PNw$/Fr3-3g8%$x}(!!=T[%>J?+]xb&9ZUqvR="

    if request.method == 'POST':
        
        serialkey = request.POST['serialkey']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if empty_field(serialkey):
            messages.error(request, 'The field serialkey is required!')
            return render(request, 'owners/signup_owner.html', status=401)

        if empty_field(name):
            messages.error(request, 'The field name is required!')
            return render(request, 'owners/signup_owner.html', status=401)

        if empty_field(email):
           messages.error(request, 'The field email is required!')
           return render(request, 'owners/signup_owner.html', status=400)

        if len(password) < 4:
            messages.error(request, 'The password needs at leats 5 caracteres!')
            return render(request, 'clients/signup_client.html', status=400)
           
        if passwords_not_match(password, password2):
            messages.error(request, 'The passwords dont match!')
            return render(request, 'owners/signup_owner.html', status=400)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken!')
            return render(request, 'owners/signup_owner.html', status=400)

        if User.objects.filter(username=name).exists():
            messages.error(request, 'Owner already taken!')
            return render(request, 'owners/signup_owner.html', status=400)

        if wrong_serial_key(serialkeyCustom, serialkey):
            messages.error(request, 'Wrong serialkey!')
            return render(request, 'owners/signup_owner.html', status=400)

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        owner = Owner.objects.create(user=user, name=user.username, email=user.email)
        messages.success(request, 'Owner successfully registered!')

        return redirect('login_owner')
    else:
        return render(request, 'owners/signup_owner.html')

def login(request):

    """ Allows owners to login  """

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if empty_field(email) or empty_field(password):
            messages.error(request, 'The fields email and password cant be blank!')
            return render(request, 'owners/login_owner.html', status=401)
            
        if Owner.objects.filter(email=email).exists() and User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password )
            if user is not None: 
                auth.login(request, user)
                return redirect('dashboard_owner')
            else:
                messages.error(request, 'Owner or password is invalid!')
                return redirect('login_owner')
        
        else:
            messages.error(request, 'Owner account not exists! ')
            return redirect('login_owner')
    
    return render(request, 'owners/login_owner.html')

def logout(request):

    """ Allows owners to logout  """

    auth.logout(request)
    return redirect('index')

def dashboard(request):

    """ Opens the area of logged owner  """

    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        movies = Movie.objects.order_by('title').filter(user=id)
        owner = Owner.objects.get(user=user)

        paginator = Paginator(movies, 3)
        page = request.GET.get('page')
        movies_by_page = paginator.get_page(page)


        data = {
            'movies': movies_by_page,
            'owner': owner
        }
        
        return render(request, 'owners/dashboard_owner.html', data)
    else:
        return redirect('index')



def empty_field(field):

    """ Avoid empty fields  """

    return not field.strip()

def passwords_not_match(password, password2):

    """ Avoid wrong match of passwords on signup window  """

    return password != password2

def wrong_serial_key(serialkey_custom, serialkey_typed):

    """ Avoid wrong serial key typed  """

    return serialkey_custom != serialkey_typed

