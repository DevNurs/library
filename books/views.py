from django.shortcuts import render
from books.models import Books


def list_of_books(request):
    books = Books.objects.all()
    return render(request, 'books/index.html', {'books': books})

