from django.contrib import admin
from .models import Attachment


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['path', 'url', 'date_created']


admin.site.register(Attachment, AttachmentAdmin)
