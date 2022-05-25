from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('articles/', views.article_list_or_create),
    path('articles/<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('articles/<int:article_pk>/like/', views.like_article),

    path('comments/<int:article_pk>/', views.create_comment),
    path('comments/<int:article_pk>/<int:comment_pk>/', views.comment_update_or_delete)

]
