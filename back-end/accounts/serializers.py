from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers

from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter

from community.models import Article
from movies.models import Movie, Collection


class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들 정의
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
        }


    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


User = get_user_model()


# 유저 정보 불러오기(블로그)
class BlogSerializer(serializers.ModelSerializer):
    class FollowFollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname', 'profile_pic')

    # 내가 쓴 게시글 확인하기 위함
    class ArticleListSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = '__all__'

        user = UserSerializer(read_only=True)

        class Meta:
            model = Article
            fields = ('pk', 'title', 'content', 'created_at', 'updated_at', 'user')
            read_only_fields = ('movie',)

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

    class CollectionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Collection
            fields = '__all__'

    collections = CollectionSerializer(many=True, read_only=True)
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
        fields = ('pk', 'status', 'profile_pic')


# 상메 업데이트
class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'status')


# 프사 업데이트
class PictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'profile_pic')

# # 닉네임 업데이트
# class NicknameUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('pk', 'nickname')






# class LikeProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('pk', 'user', 'like_users')
