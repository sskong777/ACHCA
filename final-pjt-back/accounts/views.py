from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from movies.models import Movie
# from movies.serializers.movie import FavoriteListSerializer
# from serializers.user import ProfileSerializer
# # from .serializers.user import ProfileSerializer
from .serializers import ProfileSerializer
from django.db.models import Count

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    print(serializer.data)
    return Response(serializer.data)


## 다시 수정해야함
# @api_view(['GET'])
# def favorite_list(request,username):
#     user = get_object_or_404(User,username=username)
#     favorite_movies = user.favorite_movies.all()
#     # movies = Movie.objects.annotate(
#     #     favorite_count = Count('favorite_movies', distinct=True))
#     serializer = FavoriteListSerializer(favorite_movies,many=True)
#     return Response(serializer.data)


