from rest_framework.generics import ListAPIView
from . import serializers
from . import models

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

class FilmApiView(ListAPIView):
    serializer_class = serializers.FilmSerializer

    # для порстой фильтрации
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['main_actor']

    filterset_fields = ['main_actor', 'is_published']

    def get_queryset(self):
        return models.Film.objects.all()
        # return models.Film.objects.filter(name='name_of_film')

class ActorApiView(ListAPIView):
    serializer_class = serializers.ActorSerializer

    # for more difficult requirement
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country_of_birth']

    def get_queryset(self):
        return models.Actor.objects.all()

class GenreApiView(ListAPIView):
    serializer_class = serializers.GenreSerializer

    # one more type of filters - OrderingFilter - по алфавиту/наоборот
    filter_backends = [filters.OrderingFilter]
    ordering_field = ['name']


    def get_queryset(self):
        return models.Genre.objects.all()
