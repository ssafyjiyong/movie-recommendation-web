from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogSerializer, ProfileUpdateSerializer

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)

    blog_serializer = BlogSerializer(user)

    return Response(blog_serializer.data)


@api_view(['POST'])
def following(request, user_name):
    user = get_object_or_404(User, user_name=user_name)

    if request.user in user.followings:
        user.followings.remove(request.user)
    else:
        user.followings.add(request.user)


@api_view(['PUT'])
def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.user == user:
        serializer = ProfileUpdateSerializer(
            instance=request.user, data=request.data
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)