from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('test/', views.test)
]