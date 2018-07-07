from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date_created']


admin.site.register(Contact, ContactAdmin)
