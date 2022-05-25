from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    # path('favorite/<username>/', views.favorite_list, name='favorite_list'),
]