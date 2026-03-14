from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article
from .forms import ArticleForm

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id: int):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'post': post})

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('get_article', article_id=post.id)
    else:
        form = ArticleForm()
    return render(request, 'create_post.html', {'form': form})
