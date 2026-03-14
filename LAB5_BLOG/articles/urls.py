from django.urls import path
from .views import archive, get_article, create_post

urlpatterns = [
    path('', archive, name='archive'),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('article/new/', create_post, name='create_post'),
]