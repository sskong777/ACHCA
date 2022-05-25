from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    pass
    # ## 추가
    # favorite_movies = models.ManyToManyField(Movie, related_name='favorite_users')



# class FavoriteMovie(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,releated_name='favorite_movie')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE,releated_name='favorite_movie')

