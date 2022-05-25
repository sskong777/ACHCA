from django.shortcuts import render,get_list_or_404,get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie, Review, Actor
from .serializers.movie import ActorSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer
from rest_framework import serializers
from django.db.models import Count,Avg
from django.db.models.functions import Coalesce

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    movies = Movie.objects.annotate(
        reviews_rank_avg = Avg('reviews__rank', distinct=True)
    ).all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    movie = Movie.objects.annotate(
        reviews_rank_avg = Avg('reviews__rank', distinct=True)
    ).get(pk=movie_pk)
    # movie = Movie.objects\
    #     .annotate(
    #         reviews_rank_avg = Avg(
    #         Review.objects.filter(pk=movie_pk).values('rank')))
    # print(movie)
    print(movie)
    serializer =  MovieSerializer(movie)
    return Response(serializer.data)

    
@api_view(['GET'])
def actor_detail(request, actor_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    actor = get_object_or_404(Actor, pk=actor_pk)
    # movie = Movie.objects\
    #     .annotate(
    #         reviews_rank_avg = Avg(
    #         Review.objects.filter(pk=movie_pk).values('rank')))
    # print(movie)
    
    serializer =  ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def recommended(request):
    ## 추천 알고리즘
    
    # 1.영화 평점 순
    top_vote_avg_movies = Movie.objects.all().order_by('-vote_avg')[:10]
    serializer1 = MovieListSerializer(top_vote_avg_movies, many=True)
    # return Response(serializer.data)

    # 2. 사용자 리뷰 평점 순
    top_user_rank_movies = Movie.objects.annotate(
        reviews_rank_avg = Avg('reviews__rank', distinct=True)
    ).all().order_by('-reviews_rank_avg')[:10]
    serializer2 = MovieListSerializer(top_user_rank_movies,many=True)

    # 3. 사용자 누른 좋아요(즐겨찾기) 갯수 순
    top_user_favorite_movies = Movie.objects.annotate(
        favorite_count = Count('like_users', distinct=True)
    ).all().order_by('-favorite_count')[:10]
    serializer3 = MovieListSerializer(top_user_favorite_movies,many=True)

    return Response([serializer1.data, serializer2.data, serializer3.data])



@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        # 기존 serializer 가 return 되면, 단일 review 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 review 확인 불가 => 업데이트된 전체 목록 return 
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

## 추가
@api_view(['POST'])
def favorite_movie(request,movie_pk):

    movie = get_object_or_404(Movie,pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



# Actor Follow
@api_view(['POST'])
def follow_actor(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    user = request.user
    if actor.followed_users.filter(pk=user.pk).exists():
        actor.followed_users.remove(user)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    else:
        actor.followed_users.add(user)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)