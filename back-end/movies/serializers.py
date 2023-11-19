from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, Director, Actor, Album
from community.models import Article


User = get_user_model()


class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'movie_id',
            'pk',
            'title',
            'original_language',
            'overview',
            'release_date',
            'runtime',
            'poster_path',
            'vote_average',
            'vote_count',
            'popularity',
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'movie_id',
            'pk',
            'title',
            'original_language',
            'overview',
            'release_date',
            'runtime',
            'poster_path',
            'vote_average',
            'vote_count',
            'popularity',
            'genres',
            'actors',
            'director',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

# # 영화 포스터 불러오기(HOME)
# class MoviePosterListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('pk', 'poster_path')


# # 영화 리스트 불러오기(MovieView의 목록과 필터 기능에 사용)
# class MovieListSerializer(serializers.ModelSerializer):
#     # genres = GenreSerializer(read_only=True, many=True)

#     class Meta:
#         model = Movie
#         fields = (
#             'movie_id',
#             'pk',
#             'title',
#             'original_language',
#             'overview',
#             'release_date',
#             'runtime',
#             'poster_path',
#             'vote_average',
#             'vote_count',
#             'popularity',
#         )


# # 단일 영화 상세 정보(MovieDetail)
# class MovieSerializer(serializers.ModelSerializer):
#     # 영화 좋아요 등 데이터 받기 위함
#     # class UserSerializer(serializers.ModelSerializer):
#     #     class Meta:
#     #         model = User
#     #         fields = '__all__'

#     # user = UserSerializer(read_only=True)
    
#     class CommunitySerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Article
#             # 업데이트 내역은 필요 없어서 필드에서 제외
#             fields = ('pk', 'title', 'content', 'created_at',)
#             read_only_fields = ('movie','user',)

#     class AlbumSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Album
#             fields = '__all__'  

#     # class LikeUserSerializer(serializers.ModelSerializer):
#     #     class Meta:
#     #         model = User
#     #         fields = ('pk',)
            
#     # class NormalUserSerializer(serializers.ModelSerializer):
#     #     class Meta:
#     #         model = User
#     #         fields = ('pk',)
            
#     # class HateUserSerializer(serializers.ModelSerializer):
#     #     class Meta:
#     #         model = User
#     #         fields = ('pk',)

#     # like_users = LikeUserSerializer(read_only=True, many=True)
#     # normal_users = NormalUserSerializer(read_only=True, many=True)
#     # hate_users = HateUserSerializer(read_only=True, many=True)
#     genres = GenreSerializer(read_only=True, many=True)
#     actors = ActorSerializer(read_only=True, many=True)
#     directors = DirectorSerializer(read_only=True, many=True)
#     # collections = UserSerializer(read_only=True, many=True)
#     community = CommunitySerializer(many=True)
#     album = AlbumSerializer(many=True)

#     class Meta:
#         model = Movie
#         fields = (
#             'pk',
#             'title',
#             'overview',
#             'release_date',
#             'runtime',
#             'poster_path',
#             'vote_average',
#             'vote_count',
#             # 아래 내용들은 디테일에서는 굳이 안넣어도 될 듯
#             # 'original_language',
#             # 'populatity',
#         )