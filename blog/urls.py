from django.conf.urls import url

from blog.feeds import ArticleRssFeed
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryListView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagListView.as_view(), name='tag'),
    url(r'^archives/', views.ArchivesListView.as_view(), name='archives'),
    url(r'^comment/add/(?P<article_pk>[0-9]+)/$', views.CommentAddView.as_view(), name='add_comment'),
    url(r'^rss/$', ArticleRssFeed(), name='rss'),
]
