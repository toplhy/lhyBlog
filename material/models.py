from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Attachment(models.Model):
    path = models.FileField(upload_to='material', verbose_name='素材')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '素材'
        verbose_name_plural = verbose_name

    def get_url(self):
        return reverse('media', kwargs={'path': self.path})

    url = property(get_url)
