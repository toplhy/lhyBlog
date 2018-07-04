from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Article, Category, Tag


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_queryset(self):
        return super(IndexView, self).get_queryset().filter(status=2)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    # 增加浏览量
    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        self.object.increase_count()
        return response


class CategoryListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryListView, self).get_queryset().filter(status=2).filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        context.update({'mainTitleName': category.name})
        return context


class TagListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagListView, self).get_queryset().filter(status=2).filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        context.update({'mainTitleName': tag.name})
        return context


class ArchivesListView(ListView):
    model = Article
    template_name = 'blog/archives.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        return super(ArchivesListView, self).get_queryset().filter(status=2).order_by('-date_created')
