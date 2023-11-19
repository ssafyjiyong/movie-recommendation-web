from django.shortcuts import render, get_list_or_404
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from .serializers import MovieSearchSerializer, MovieDetailSerializer, GenreSerializer, ActorSerializer, DirectorSerializer, AlbumSerializer
from .models import Actor, Album, Director, Genre, Movie
from .spotify_config import getHeaders

import requests

# API 목록
TMDB_API_KEY = settings.TMDB_API_KEY
KOFIC_API_KEY = settings.TMDB_API_KEY


@api_view(['GET'])
def movie_search(request, movie_title):
    # 검색 결과를 저장할 배열
    search_results = []

    # 장고 DB에 있는 영화 목록
    movies = Movie.objects.all()

    for movie in movies:
        # 검색내용의 공백 및 서버에 저장된 영화 제목의 공백을 제거하여 문자열 확인
        if movie_title.replace(" ", "") in movie.title.replace(" ", ""):
            serializer = MovieSearchSerializer(movie)
            search_results.append(serializer.data)
    
    # 장고서버에 검색결과가 존재하지 않을 경우 api를 호출하여 한번 더 검색
    if not search_results:
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=ko-KR&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }

        results = requests.get(url, headers=headers).json()['results']

        # api서버에 검색결과가 존재할 경우 장고 서버에 저장 후 검색 결과 배열에 한번 더 저장
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

            serializer = MovieSearchSerializer(data=fields)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                search_results.append(serializer.data)

    # 검색 결과 배열을 리턴
    return Response(search_results)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    genres = Genre.objects.values_list('name', flat=True)
    actors = Actor.objects.values_list('name', flat=True)
    directors = Director.objects.values_list('name', flat=True)

    # detail 조회가 처음이 아닌 영화의 경우 바로 디테일 값을 리턴
    if movie.genres == [] or movie.actors == [] or movie.director == []:
        serializer = MovieDetailSerializer(movie)

        return Response(serializer.data)
    
    # 처음 조회하는 영화일 경우 장르, 배우, 감독 필드를 채워줌

    else:
        # 장르
        if movie.genres == [] or movie.runtime == None or movie.original_title == None:
        
            # 장르 정보 및 런닝 타임을 불러오기 위한 요청
            url = f"https://api.themoviedb.org/3/movie/{movie_id}"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {TMDB_API_KEY}"
            }

            results = requests.get(url, headers=headers).json()

            # 런닝 타임 업데이트
            movie.runtime = results['runtime']
            movie.original_title = results['original_title']
            movie.save()

            # 장르 목록을 순회하며 등록
            for res_genre in results['genres']:
                # 장고DB에 없는 장르일 경우 장르 테이블을 새롭게 생성
                if res_genre['name'] not in genres:
                    fields = {
                        'name': res_genre['name']
                    }

                    genre_serializer = GenreSerializer(data=fields)
                    
                    if genre_serializer.is_valid(raise_exception=True):
                        genre_serializer.save()

                # 영화의 장르 필드에 조회된 장르값을 추가(ManyToMany)
                movie.genres.add(Genre.objects.get(name=res_genre['name']))

        # 배우, 감독
        if movie.actors != [] or movie.director != []:
            # 영화 출연진, 감독을 불러오기 위한 요청
            url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {TMDB_API_KEY}"
            }

            results_actors = requests.get(url, headers=headers).json()['cast']
            results_directors = requests.get(url, headers=headers).json()['crew']


            # 배우
            for result in results_actors:
                if result["known_for_department"] == "Acting":
                    if result['name'] not in actors:
                        fields = {
                            'name': result['name'],
                            'profile_path': result['profile_path'], 
                        }

                        actor_serializer = ActorSerializer(data=fields)

                        if actor_serializer.is_valid(raise_exception=True):
                            actor_serializer.save()

                    movie.actors.add(Actor.objects.get(name=result['name']))

            # 감독
            for result in results_directors:
                if result["job"] == "Director":
                    if result['name'] not in directors:
                        fields = {
                            'name': result['name'],
                            'profile_path': result['profile_path'], 
                        }

                        director_serializer = DirectorSerializer(data=fields)

                        if director_serializer.is_valid(raise_exception=True):
                            director_serializer.save()
                    
                    movie.director.add(Director.objects.get(name=result['name']))
        
        # 앨범정보
        try:
            album = Album.objects.get(movie_id=movie.id)
        except:
            url = 'https://api.spotify.com/v1/search'
            headers = getHeaders()
            
            # 영화 OST 검색 쿼리 파라미터
            params = {
                'q': f'{movie.original_title} ost',
                'type': 'album'
            }

            response = requests.get(url, headers=headers, params=params)
            data = response.json()['albums']['items'][0]

            fields = {
                'movie': movie.id,
                'name': data['name'],
                'image': data['images'][0]['url'],
                'url': data['external_urls']['spotify'],
            }
            
            serializer = AlbumSerializer(data=fields)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)        


