from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('<str:user_name>/', views.profile),
    path('<str:user_name>/following/', views.following),
    path('<int:user_pk>/update_nickname/', views.update_nickname),
    path('<int:user_pk>/update_status/', views.update_status),
    path('<int:user_pk>/update_picture/', views.update_picture),
]
