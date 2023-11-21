from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies),
    path('genres/', views.genres),
    path('actors/', views.actors),
    path('directors/', views.directors),
    path('<int:page>/', views.movie_page),
    path('movie_search/<str:movie_title>/', views.movie_search),
    path('movie_detail/<int:movie_id>/', views.movie_detail),
    path('movie_detail/<int:movie_id>/like/', views.movie_like),
    path('movie_detail/<int:movie_id>/soso/', views.movie_normal),
    path('movie_detail/<int:movie_id>/hate/', views.movie_hate),
]
