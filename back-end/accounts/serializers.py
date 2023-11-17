from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from community.models import Article

User = get_user_model()

# 유저 정보 불러오기(네비게이션바)
class UserNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')


# 유저 정보 불러오기(프로필)
class ProfileSerializer(serializers.ModelSerializer):
    class FollowFollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    # 내가 쓴 게시글 확인하기 위함
    class ArticleListSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = '__all__'

        user = UserSerializer(read_only=True)

        class Meta:
            model = Article
            fields = ('pk', 'title', 'content', 'created_at', 'updated_at',)
            read_only_fields = ('movie','user',)

    # 좋아요한 영화만 프로필에 표시 하기 위함
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                # 필요한 필드 나중에 추가
                'pk',
                'title',
                'poster_path',
                'release_date',
            )

    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(
        source='followers.count', read_only=True
    )
    following_count = serializers.IntegerField(
        source='followings.count', read_only=True
    )
    articles = ArticleListSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    articles_count = serializers.IntegerField(
        source='articles.count', read_only=True
    )
    like_movies_count = serializers.IntegerField(
        source='like_movies.count', read_only=True
    )

    class Meta:
        model = User
        fields = '__all__'


# 프로필 업데이트
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'profile_pic', 'status')


class LikeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'user', 'like_users')
