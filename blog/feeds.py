from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Article


class ArticleRssFeed(Feed):

    title = "toplhyi的博客"
    link = "/rss/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:detail', kwargs={'pk': item.pk})
