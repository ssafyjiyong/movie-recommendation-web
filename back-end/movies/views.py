from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer

from datetime import datetime

import requests


# Create your views here.


@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        api_key = settings.TMDB_API_KEY
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # return Response(requests.get(url, headers=headers).json())

        movies = requests.get(url, headers=headers).json()['results']

        for movie in movies:
            fields = {
                'movie_id': movie['id'],
                'title': movie['title'],
                'original_language': movie['original_language'],
                'overview': movie['overview'],
                'release_date': movie["release_date"],
                'poster_path': movie['poster_path'],
                'vote_average': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'video': movie['video'],
                'popularity': movie['popularity'],
                'genres': movie['genre_ids'],
            }
            

            # return Response(fields)
            serializer = MovieListSerializer(data=fields)
            if not serializer.is_valid():
                return Response(serializer.errors)
            else:
                serializer.save()

        return Response('success')
                
        

        # return Response(movies)


        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()

        #     return Response(serializer.data)
