import markdown
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import TocExtension

from blog.forms import CommentForm
from blog.models import Article, Category, Tag


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 5

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

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                           'markdown.extensions.codehilite',
                                           TocExtension(slugify=slugify)])
        article.content = md.convert(article.content)
        article.toc = md.toc
        return article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comments = self.object.comment_set.all()
        context.update({
            'form': form,
            'comments': comments
        })
        return context


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


class CommentAddView(View):
    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.save()
                return redirect('blog:detail', article.pk)
            else:
                comments = article.comment_set.all()
                context = {
                    'article': article,
                    'form': form,
                    'comments': comments,
                }
                return render(request, 'blog/detail.html', context=context)
        return redirect('blog:detail', article.pk)
