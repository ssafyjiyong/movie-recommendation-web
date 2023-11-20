from django.urls import path
from . import views


app_name = 'profile'
urlpatterns = [
    path('<str:user_name>/', views.profile),
]
