from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='inicio'),
    path('peliculas/<int:id>/', views.detalle_pelicula, name='detalle'),
]