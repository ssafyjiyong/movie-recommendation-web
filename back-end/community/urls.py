from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('caht/', views.articles),
    path('article_detail/<int:article_pk>/', views.article_detail),
    path('article_detail/<int:article_pk>/comment/', views.comment),
    path('article_detail/<int:article_pk>/comment/<int:comment_pk>/', views.comment_delete),
    # path('article_detail/<int:article_pk>/comment/<int:comment_pk>/recomment/', views.recomment),
    # path('article_detail/<int:article_pk>/comment/<int:comment_pk>/recomment/<int:recomment_pk>/', views.recomment_delete),
]
