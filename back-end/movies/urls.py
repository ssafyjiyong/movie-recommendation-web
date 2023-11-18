from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # path('test/', views.test)
    path('movie_search/<str:movie_title>/', views.movie_search),
    path('movie_detail/<int:movie_id>/', views.movie_detail),
]
