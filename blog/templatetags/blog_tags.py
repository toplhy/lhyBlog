from django.db.models import Count

from blog.models import Article, Category, Tag
from django import template

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.filter(status=2).all().order_by('-date_created')[:num]


@register.simple_tag
def archives(num=5):
    return Article.objects.filter(status=2).dates('date_created', 'month', order='DESC')[:num]


@register.simple_tag()
def get_categories(num=5):
    return Category.objects.annotate(article_num=Count('article')).filter(article__status=2)[:num]


@register.simple_tag()
def count_category():
    return Category.objects.annotate(article_num=Count('article')).filter(article__status=2).count()


@register.simple_tag()
def count_articles():
    return Article.objects.filter(status=2).count()


@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(article_num=Count('article')).filter(article_num__gt=0)
