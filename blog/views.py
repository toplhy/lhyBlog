from django.shortcuts import render, get_object_or_404
from blog.models import Article


def index(request):
    articles = Article.objects.all().filter(status='1').order_by('-date_created')
    return render(request, 'blog/index.html', context={'articles': articles})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', context={'article': article})
