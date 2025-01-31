from django.urls import path, include
from . import views
from . import api

urlpatterns = [
    path('film', api.FilmApiView.as_view(), name='api_film'),
    path('actor', api.ActorApiView.as_view(), name='api_actor'),
    path('genre', api.GenreApiView.as_view(), name='api_genre'),
    path('films/', views.film_index, name='film_index'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
]
