from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)



class Actor(models.Model):
    # movies = models.ManyToManyField('movie', related_name='actors_movies')
    actor_name = models.CharField(max_length=50)
    img_key = models.CharField(max_length=100, null=True)
    credit_id = models.CharField(max_length=100, null=True)
    followed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_actors')


# class Actor(models.model):
#     cast = models.JSONField()
#     crew = models.JSONField()

    
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)
    # actors = models.JSONField(null=True)
    director = models.CharField(max_length=100, null=True)
    video_key = models.CharField(max_length=100, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    def __str__(self):
        return f'{self.movie}({self.title})'