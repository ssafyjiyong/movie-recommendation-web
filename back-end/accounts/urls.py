from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('<str:user_name>/', views.profile),
    path('blog/<str:user_name>/', views.blog),
    path('<str:nickname>/following/', views.following),
    path('<int:user_pk>/update_profile/', views.update_profile),
    # path('<int:user_pk>/update_status/', views.update_status),
    # path('<int:user_pk>/update_picture/', views.update_picture),
]
