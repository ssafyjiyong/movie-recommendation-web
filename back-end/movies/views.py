from django.shortcuts import render
from rest_framework.response import Response

from .serializers import MovieListSerializer
import requests

# Create your views here.
def test(request):

    if request.method == 'GET':
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjIwOTNlMzAxNzQ3ZDRhN2VlOWQ4YTQzYWFiOTU4ZCIsInN1YiI6IjY1M2Y1ZjhkNTE5YmJiMDBhYjY5ZDAwNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QwAbBLNPgnnmD1rEtxVWPLpZpxpN7C_4ow8tYzcjaXY"
        }

        response = requests.get(url, headers=headers)

        return Response(response.text)

        # serializer = MovieListSerializer(data=response.data)
        
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()

        #     return Response(serializer.data)