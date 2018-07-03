from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryListView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagListView.as_view(), name='tag'),
]
