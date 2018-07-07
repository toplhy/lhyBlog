from django.shortcuts import render, redirect
from django.views.generic.base import View

from contact.froms import ContactForm


def index(request):
    return render(request, 'contact.html')


class ContactAddView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save()
                return redirect('contact:index')
            else:
                data = {
                    'name': request.POST['name'],
                    'email': request.POST['email'],
                    'subject': request.POST['subject'],
                    'content': request.POST['content'],
                }
                context = {
                    'form': form,
                    'data': data,
                }
                return render(request, 'contact.html', context=context)
        return redirect('contact:index')
