from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('home', home, name='home'),
    path('', register, name='register'),
    path('status/', home2, name='status'),  
    path('client/', create_client, name='client'),  
    path('clientview/', clientview, name='clientview'),  
    path('contact/', home3, name='contact'),
    path('hola/', hola, name='hola'),
    path('search/', main, name='search'),
    path('contact_view/', contact_view, name='contact_view'),
    path('genpdf/', generate_pdf, name='genpdf'),   
    path('logout/', logout_view, name='logout'),

    # Other URL patterns... 
]