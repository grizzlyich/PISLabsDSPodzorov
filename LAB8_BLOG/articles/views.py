from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Article
from .forms import ArticleForm


def archive(request):
    posts = Article.objects.all()
    return render(request, "archive.html", {"posts": posts})


def get_article(request, article_id: int):
    post = get_object_or_404(Article, id=article_id)
    return render(request, "article.html", {"post": post})


def create_post(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("get_article", article_id=post.id)
    else:
        form = ArticleForm()

    return render(request, "create_post.html", {"form": form})


def edit_post(request, article_id: int):
    post = get_object_or_404(Article, id=article_id)

    if not request.user.is_authenticated or request.user != post.author:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("get_article", article_id=post.id)
    else:
        form = ArticleForm(instance=post)

    return render(request, "edit_post.html", {"form": form, "post": post})


def delete_post(request, article_id: int):
    post = get_object_or_404(Article, id=article_id)

    if not request.user.is_authenticated or request.user != post.author:
        raise Http404

    # GET -> показать страницу подтверждения
    # POST -> удалить
    if request.method == "POST":
        post.delete()
        return redirect("archive")

    return render(request, "delete_post.html", {"post": post})


# ---------- AUTH ----------

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        errors = []
        if not username:
            errors.append("Введите логин")
        if User.objects.filter(username__iexact=username).exists():
            errors.append("Такой логин уже занят")
        if not password:
            errors.append("Введите пароль")

        if errors:
            return render(
                request,
                "register.html",
                {"errors": errors, "username": username, "email": email},
            )

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect("archive")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(
                request,
                "login.html",
                {"error": "Неверный логин или пароль", "username": username},
            )

        login(request, user)
        return redirect("archive")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("archive")