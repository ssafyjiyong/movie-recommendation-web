from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogSerializer

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)

    blog_serializer = BlogSerializer(user)

    return Response(blog_serializer.data)