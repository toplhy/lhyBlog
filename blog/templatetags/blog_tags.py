from blog.models import Article, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-date_created')[:num]


@register.simple_tag
def archives(num=5):
    dates = []
    for date in Article.objects.dates('date_created', 'month', order='DESC')[:num]:
        dict = {'year': date.year, 'month': date.month,
                'count': Article.objects.filter(date_created__year=date.year, date_created__month=date.month).count()}
        dates.append(dict)
    return dates


@register.simple_tag
def count_archives(num=5):
    return Article.objects.dates('date_created', 'month').count()


@register.simple_tag()
def get_categories(num=5):
    categories = []
    for category in Category.objects.all()[:num]:
        dict = {'name': category.name, 'count': Article.objects.filter(category=category).count()}
        categories.append(dict)
    return categories


@register.simple_tag()
def count_category():
    return Category.objects.count()