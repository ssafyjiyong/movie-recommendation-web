from django.shortcuts import render, get_list_or_404
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer
from .models import Actor, Album, Director, Genre, Movie

import requests

# API 목록
TMDB_API_KEY = settings.TMDB_API_KEY
KOFIC_API_KEY = settings.TMDB_API_KEY
SPOTIFY_API_KEY = settings.TMDB_API_KEY

# django 서버에 저장된 데이터들
# NOMAD_ACTORS = get_list_or_404(Actor)
# NOMAD_ALBUMS = get_list_or_404(Album)
# NOMAD_DIRECTORS = get_list_or_404(Director)
# NOMAD_GENRES = get_list_or_404(Genre)
NOMAD_MOVIES = get_list_or_404(Movie)
# NOMAD_MOVIES = Movie.objects.all()


@api_view(['GET'])
def movie_search(request, movie_title):
    search_results = []

    for movie in NOMAD_MOVIES:
        if movie_title in movie.title:
            serializer = MovieListSerializer(movie)
            search_results.append(serializer.data)
    
    if not search_results:
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=ko-KR&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }

        results = requests.get(url, headers=headers).json()['results']

        for result in results:
            fields = {
                'movie_id': result['id'],
                'title': result['title'],
                'original_language': result['original_language'],
                'overview': result['overview'],
                'release_date': result["release_date"],
                'poster_path': result['poster_path'],
                'vote_average': result['vote_average'],
                'vote_count': result['vote_count'],
                'video': result['video'],
                'popularity': result['popularity'],
                'genres': result['genre_ids'],
            }

            serializer = MovieListSerializer(data=fields)
            if not serializer.is_valid():
                return Response(serializer.errors)
            else:
                serializer.save()
                search_results.append(serializer.data)

    return Response(search_results)




# TMDB_API 개봉예정작 영화목록 받아오는 코드
# @api_view(['GET'])
# def test(request):
#     if request.method == 'GET':
#         api_key = settings.TMDB_API_KEY
#         url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

#         headers = {
#             "accept": "application/json",
#             "Authorization": f"Bearer {api_key}"
#         }

#         movies = requests.get(url, headers=headers).json()['results']

#         for movie in movies:
#             fields = {
#                 'movie_id': movie['id'],
#                 'title': movie['title'],
#                 'original_language': movie['original_language'],
#                 'overview': movie['overview'],
#                 'release_date': movie["release_date"],
#                 'poster_path': movie['poster_path'],
#                 'vote_average': movie['vote_average'],
#                 'vote_count': movie['vote_count'],
#                 'video': movie['video'],
#                 'popularity': movie['popularity'],
#                 'genres': movie['genre_ids'],
#             }
            

#             # return Response(fields)
#             serializer = MovieListSerializer(data=fields)
#             if not serializer.is_valid():
#                 return Response(serializer.errors)
#             else:
#                 serializer.save()

#         return Response('success')
                
        
