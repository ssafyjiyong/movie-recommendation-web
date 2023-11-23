from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogSerializer, ProfileUpdateSerializer, StatusUpdateSerializer, PictureUpdateSerializer

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)

    blog_serializer = BlogSerializer(user)

    return Response(blog_serializer.data)


@api_view(['POST'])
def following(request, nickname):
    user = get_object_or_404(User, nickname=nickname)

    if request.user != user:
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return Response("팔로우 또는 취소 성공")


@api_view(['PUT'])
def update_profile(request, user_pk):
    user = get_object_or_404(User, id=user_pk)

    if request.user == user:
        serializer = ProfileUpdateSerializer(
            instance=request.user, data=request.data
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)


@api_view(['PUT'])
def update_status(request, user_pk):
    user = get_object_or_404(User, id=user_pk)

    if request.user == user:
        serializer = StatusUpdateSerializer(
            instance=request.user, data=request.data
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            return Response(serializer.data)


@api_view(['POST', 'PUT'])
def update_picture(request, user_pk):
    user = get_object_or_404(User, id=user_pk)
    me = request.user

    if request.method == 'PUT':
        if me == user:
            serializer = PictureUpdateSerializer(
                instance=request.user, data=request.data
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'POST':
        if me == user:
            serializer = PictureUpdateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def blog(request, user_name):
    user = get_object_or_404(User, nickname=user_name)
    serializer = BlogSerializer(user)

    return Response(serializer.data)


@api_view(['DELETE'])
def signout(request, nickname):
    user = get_object_or_404(User, nickname=nickname)

    if request.user == user:
        user.delete()
        return Response("회원탈퇴 완료")