from django.urls import path
from . import views

app_name ='movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('actor/<int:actor_pk>/', views.actor_detail),
    # actor follow
    path('actor/<int:actor_pk>/follow/', views.follow_actor),

    path('recommended/', views.recommended, name='recommended'),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    ## 추가
    path('<int:movie_pk>/favorite/', views.favorite_movie),
    
]