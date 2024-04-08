from django.urls import path
from . import views

urlpatterns = [
    # set endpoints urls and it calls functions in views.py 
    path('', views.getData),
    # add new url to new end point
    path('add/', views.addItem)
]