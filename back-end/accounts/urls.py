from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<str:user_name>/', views.profile),
    path('<str:nickname>/following/', views.following),
    path('<int:user_pk>/update_profile/', views.update_profile),
    # path('<int:user_pk>/update_status/', views.update_status),
    # path('<int:user_pk>/update_picture/', views.update_picture),
]
