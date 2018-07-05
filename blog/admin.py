from django.contrib import admin
from .models import Category, Tag, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'count', 'status', 'last_updated']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'article', 'content', 'date_created']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
