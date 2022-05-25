from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Actor
from community.models import Article
from movies.models import Movie,Review
from movies.views import favorite_movie
from movies.serializers.movie import MovieSerializer
from movies.serializers.movie import ReviewSerializer
from movies.serializers.movie import ActorSerializer


class ProfileSerializer(serializers.ModelSerializer):


    class ArticleSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('pk', 'username')

        user = UserSerializer(read_only=True)
        like_users = UserSerializer(read_only=True, many=True)
        class Meta:
            model = Article
            fields = ('pk', 'user', 'title', 'content', 'comments', 'like_users', 'created_at', 'updated_at')
            
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk', 'title', 'content', 'movie', 'rank')
    articles = ArticleSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields =('pk', 'actor_name', 'img_key')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields=('id', 'title', 'poster_path')

    # following_actors 추가
    following_actors = ActorSerializer(many=True)

    ## 추가(수정)
    favorite_movies = MovieSerializer(many=True)
    # favorite_movies = MovieSerialiser(many=True)
    like_articles = ArticleSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles','favorite_movies','reviews','following_actors',)




# class ProfileSerializer(serializers.ModelSerializer):

#     class ArticleSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Article
#             fields = ('pk', 'title','content',)

#     like_reviews = ReviewSerializer(many=True)
#     user_reviews = ReviewSerializer(many=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('pk', 'username', 'like_reviews', 'user_reviews',)
# # 



# from rest_framework import serializers
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from community.models import Review

# class ProfileSerializer(serializers.ModelSerializer):

#     class ReviewSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Review
#             fields = ('pk', 'movie_title','content','rank')

#     like_reviews = ReviewSerializer(many=True, read_only=True)
#     user_reviews = ReviewSerializer(many=True, read_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('pk', 'username', 'like_reviews', 'user_reviews',)
