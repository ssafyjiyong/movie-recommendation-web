from django.urls import path
from . import views


app_name = 'profile'
urlpatterns = [
    path('<str:user_name>/', views.profile),
    path('<str:user_name>/following/', views.following),
]
