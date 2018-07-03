from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名称')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    STATUS_CHOICES = (
        ('1', '草稿'),
        ('2', '发布'),
        ('3', '废弃'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(default='', verbose_name='正文')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='摘要')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    count = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='状态')
    author = models.CharField(max_length=20, null=True, verbose_name='作者')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建时间')
    last_updated = models.DateField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_count(self):
        self.count += 1
        self.save(update_fields=['count'])
