from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Movie

from .models import Article, Comment, Recomment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, RecommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def articles(request):
    # 전체 게시글 목록 조회
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)

        return Response(serializer.data)
    # 게시글 등록
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile_articles(request, user_name):
    user = get_object_or_404(get_user_model(), nickname=user_name)
    articles = Article.objects.filter(user=user).order_by('-pk')
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def movie_articles(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    articles = Article.objects.filter(movie=movie)
    
    serializer = ArticleListSerializer(articles, many=True)

    return Response(serializer.data)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 단일 게시글 정보 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 게시글 좋아요
    elif request.method == 'POST':
        if request.user in article.like_users:
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 수정
    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    # 삭제        
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response("삭제 완료")


@api_view(['POST'])
def article_like(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.user in article.like_users:
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    serializer = ArticleSerializer(article)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        comment = Comment.objects.filter(article = article)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)

            return Response(serializer.data)


@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if comment.user == request.user:
        comment.delete()
    
    return Response("삭제되었습니다.")


@api_view(['GET', 'POST'])
def recomment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        recomments = Recomment.objects.filter(comment=comment)
        serializer = RecommentSerializer(recomments, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(comment=comment)

            return Response(serializer.data)
        

@api_view(['DELETE'])
def recomment_delete(request, article_pk, comment_pk, recomment_pk):
    recomment = Recomment.objects.get(pk=recomment_pk)

    if request.user == recomment.user:
        recomment.delete()

        return Response("삭제되었습니다.")