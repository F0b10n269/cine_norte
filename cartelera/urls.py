from django.urls import path

from . import views

urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
]