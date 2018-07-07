from django.conf.urls import url
from . import views

app_name = 'contact'
urlpatterns = [
    url(r'^contact/', views.index, name='index'),
    url(r'^add_contact/', views.ContactAddView.as_view(), name='add_contact'),
]
