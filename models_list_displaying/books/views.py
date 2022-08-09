from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)

def date_view(request, pub_date):
    template = 'books/date_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').values('pub_date').first()
    prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').values('pub_date').first()
    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context) 