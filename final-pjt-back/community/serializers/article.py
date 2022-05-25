from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from .comment import CommentSerializer

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_users', 'created_at', 'updated_at')


# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count', 'created_at', 'updated_at')








# from dataclasses import field
# from ..models import  Review
# from movies.models import Movie
# from rest_framework import serializers
# from django.conf import settings
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class MovieReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title',)


# class ReviewListSerializer(serializers.ModelSerializer):

#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk','username',)

        
#     movie = MovieReviewSerializer(read_only=True)
#     user = UserSerializer(read_only=True)
    
#     class Meta:
#         model = Review
#         fields = ('movie','user','movie_title','content','rank',)



# class ReviewSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk','username',)

#     movie = MovieReviewSerializer(read_only=True)
#     user = UserSerializer(read_only = True)
#     class Meta:
#         model = Review
#         fields = ('movie','user','movie_title','content','rank',)
