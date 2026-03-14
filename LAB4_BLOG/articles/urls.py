from django.urls import path
from .views import archive, get_article

urlpatterns = [
    path('', archive, name='archive'),
    path('article/<int:article_id>/', get_article, name='get_article'),
]