# Introduction

This project is a  site of a moviestore, that provides security, dinamic management of rented movies
by owners and a friendly template for clients. 

This project is written with django 3.1.6 and python 3 in mind.

![alt text](https://i.ibb.co/JKsn0WM/download.png)
### Main features

* Separated enviromnent of clients and owners

* The clients have their own dashboard to manage and look their rented movies

* Bootstrap static files included

* Custom owner and client signup, login and logout

* Complete CRUD for owners, with dynamic forms and soft buttons

* The clients can rent a movie, cancel it or look for details of renting

* The movies are listed by title and genre

* Local sqlite3 db

* Variety of options on creation of a movie, like Description and image


# Usage

To start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
Serial Key for register new owners: g\C_%8=5*;?z:6J+@uW_4+3_nj3r=?qY_6HG!%PNw$/Fr3-3g8%$x}(!!=T[%>J?+]xb&9ZUqvR=
