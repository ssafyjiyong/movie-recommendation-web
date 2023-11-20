from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import render

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def articles(request):
    # 전체 게시글 목록 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)

        return Response(serializer.data)
    # 게시글 등록
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


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



