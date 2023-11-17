from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, Actor
from community.models import Article, Comment, Recomment, Image

User = get_user_model()


# 커뮤니티 게시글 목록(CommunityView)
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
    
    class ReommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recomment
            fields = ('pk', 'content', 'created_at',)
            read_only_fields = ('comment','user',)
    
    class ImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = Image
            fields = ('pk', 'article_image')

    comments = CommentSerializer(read_only=True, many=True)
    recomments = ReommentSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie', 'user',)