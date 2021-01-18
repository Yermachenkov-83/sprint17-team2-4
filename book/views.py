from django.shortcuts import render, redirect
from .models import Book
from author.models import Author


def index(request):
    books = Book.objects.order_by('-id')

    return render(
        request,
        'book/index.html',
        {'title': 'Книги', 'books': books}
    )


def detail(request, book_id):
    book = Book.get_by_id(book_id)
    context = {
        'title': f'Книга "{book.name}"',
        'book': book
    }

    return render(
        request,
        'book/detail.html',
        context
    )


