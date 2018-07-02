from django.contrib import admin
from .models import Category, Tag, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'count', 'status', 'last_updated' ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
