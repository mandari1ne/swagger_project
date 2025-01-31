from rest_framework import serializers
from . import models

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Film
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'
