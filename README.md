# Django_REST_Framework


Django REST Framework

Referred :
Youtube video 
Django REST Framework Oversimplified  
By Author- Dennis Ivy


https://youtu.be/cJveiktaOSQ


*** Commands to create Django project ***
PS H:\Python\Gan_coding\Django_projects> python -m venv django_env
PS H:\Python\Gan_coding\Django_projects> H:\Python\Gan_coding\Django_projects\django_env\Scripts\Activate.ps1
(django_env) PS H:\Python\Gan_coding\Django_projects> pip install django

(django_env) PS H:\Python\Gan_coding\Django_projects> django-admin startproject myproject
(django_env) PS H:\Python\Gan_coding\Django_projects> pip install djangorestframework

(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py runserver

Open browser and type http://127.0.0.1:8000/
U will get API response
{"name":"Dennis", "age":28}


Above is static data response

-- Now lets create startapp base that creates dynamic data
(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py startapp base

Once models are created  lets go and run some migrations
(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py makemigrations
Migrations for 'base':
  base\migrations\0001_initial.py
    - Create model Item


--Apply all these migrations by calling migrate command
(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, base, contenttypes, sessions


-- To add some data, lets open Interactive shell to work with our data
(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py shell
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from base.models import Item
>>> Item.objects.create(name="Item #1") 
<Item: Item object (1)>
>>> Item.objects.create(name="Item #2") 
<Item: Item object (2)>
>>> Item.objects.create(name="Item #3") 
<Item: Item object (3)>
>>> items = Item.objects.all()
>>> print(items)
<QuerySet [<Item: Item object (1)>, <Item: Item object (2)>, <Item: Item object (3)>]>
>>> exit()


(django_env) PS H:\Python\Gan_coding\Django_projects\myproject> python manage.py runserver   


