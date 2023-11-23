from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('article_list/', views.articles),
    path('article_list/<str:user_name>/', views.profile_articles),
    path('article_list/movie/<int:movie_id>/', views.movie_articles),
    path('article_detail/<int:article_pk>/', views.article_detail),
    path('article_detail/<int:article_pk>/article_like/', views.article_like),
    path('article_detail/<int:article_pk>/comment/', views.comment),
    path('article_detail/<int:article_pk>/comment/<int:comment_pk>/', views.comment_delete),
    path('article_detail/<int:article_pk>/comment/<int:comment_pk>/recomment/', views.recomment),
    path('article_detail/<int:article_pk>/comment/<int:comment_pk>/recomment/<int:recomment_pk>/', views.recomment_delete),
]
