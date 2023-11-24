from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, Actor
from community.models import Article, Comment, Recomment

User = get_user_model()

# 커뮤니티 게시글 목록(CommunityView)
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'

# # 게시글 이미지
# class ArticleImageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(use_url=True)

#     class Meta:
#         model = Image
#         fields = [
#             'image',
#         ]


# 단일 게시글(CommunityDetail)
class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('pk', 'content', 'created_at',)
            read_only_fields = ('article','user',)
    
    class RecommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recomment
            fields = ('pk', 'content', 'created_at',)
            read_only_fields = ('comment','user',)

    comments = CommentSerializer(read_only=True, many=True)
    recomments = RecommentSerializer(read_only=True, many=True)
    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname', 'profile_pic', 'followings', 'followers',)

    user = UserSerializer(read_only=True)
    
    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    class RecommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recomment
            fields = '__all__'

    recomment = RecommentSerializer(read_only=True)

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('article','user',)


class RecommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname', 'profile_pic')

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Recomment
        fields = ('pk', 'content', 'created_at', 'user')
        read_only_fields = ('comment',)