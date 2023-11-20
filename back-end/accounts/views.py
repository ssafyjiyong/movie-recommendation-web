from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import 

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    