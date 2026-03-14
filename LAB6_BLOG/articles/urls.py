from django.urls import path
from .views import (
    archive,
    get_article,
    create_post,
    edit_post,
    delete_post,
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path("", archive, name="archive"),
    path("article/<int:article_id>/", get_article, name="get_article"),

    # создание
    path("article/new/", create_post, name="create_post"),

    # редактирование / удаление
    path("article/<int:article_id>/edit/", edit_post, name="edit_post"),
    path("article/<int:article_id>/delete/", delete_post, name="delete_post"),

    # авторизация
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]