from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    subject = models.CharField(max_length=100, verbose_name='主题')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    content = models.TextField(default='', verbose_name='正文')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '联系我'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject

