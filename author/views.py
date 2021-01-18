from django.shortcuts import render, redirect
from .models import Author
from book.models import Book


def index(request):
    authors = Author.objects.order_by('-id')

    return render(
        request,
        'author/index.html',
        {'title': 'Авторы', 'authors': authors}
    )


def detail(request, author_id):
    author = Author.get_by_id(author_id)
    books = Book.objects.filter(authors__id=author_id)
    context = {
        'title': f'{author.get_full_name()}',
        'author': author,
        'books': books
    }

    return render(
        request,
        'author/detail.html',
        context
    )

