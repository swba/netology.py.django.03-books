import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render, redirect

from books.models import Book


def index_view(request):
    return redirect('books')

def books_view(request: WSGIRequest, date: datetime.date = None):
    template = 'books/books_list.html'

    query = Book.objects
    if date:
        dates = query.values('pub_date').order_by('pub_date').distinct('pub_date')
        dates = [item['pub_date'] for item in dates]
        try:
            index = dates.index(date)
        except ValueError:
            raise Http404('Incorrect publish date')
        context = {
            'books': query.filter(pub_date=date).order_by('pub_date'),
            'nav': {
                'prev': dates[index - 1] if index > 0 else None,
                'curr': date,
                'next': dates[index + 1] if index < len(dates) - 1 else None,
            }
        }
    else:
        context = {
            'books': query.all().order_by('pub_date')
        }

    return render(request, template, context)
