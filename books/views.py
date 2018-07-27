from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
from PMSYS.forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import ListView
from books.models import Publisher


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        qv = request.GET['q']
        books = Book.objects.filter(title__contains=qv)
        return render(request, 'search_result.html', {'books': books, 'query': qv})

    else:
        return render(request, 'search_form.html', {'error': True})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@tu.com'),
                ['siteowner@tu.com']
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial={'subject': 'i love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'myfavoritepublisher'