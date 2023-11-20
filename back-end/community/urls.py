from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('caht/', views.articles),
    path('article_detail/<int:article_pk>/', views.article_detail),
]
