from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    # birth_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Film(models.Model):
    # name = models.CharField(max_length=100)
    # description = models.TextField()
    # release_year = models.PositiveIntegerField()
    #
    price = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
    #
    # main_actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=90)
    date_of_creation = models.DateField(null=True, blank=True)
    main_actor = models.ForeignKey('Actor', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=False)
    genre = models.ForeignKey('Genre', to_field='name', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
