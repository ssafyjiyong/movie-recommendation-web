from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movielist/', views.movies),
    path('genres/', views.genres),
    path('genres/<int:movie_id>/', views.movie_genres),
    path('collections/', views.collections),
    path('<int:page>/', views.movie_page),
    path('directors/<int:movie_id>/', views.directors),
    path('actors/<int:movie_id>/', views.actors),
    path('collections/<int:collection_id>/', views.collections_delete),
    path('collections/<int:movie_id>/', views.movie_collections),
    path('collections/<int:user_id>/', views.user_collections),
    path('collections/<int:collection_id>/<int:movie_id>/', views.collections_update),
    path('movie_search/<str:movie_title>/', views.movie_search),
    path('movie_detail/<int:movie_id>/', views.movie_detail),
    path('movie_detail/<int:movie_id>/following/', views.movie_mate),
    path('movie_detail/<int:movie_id>/album/', views.movie_album),
    path('movie_detail/<int:movie_id>/like/', views.movie_like),
    path('movie_detail/<int:movie_id>/soso/', views.movie_normal),
    path('movie_detail/<int:movie_id>/hate/', views.movie_hate),
]
