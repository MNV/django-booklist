from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from booklist.models import Book, Author


def home(request):
    """Главная страница. Редирект на `/books`"""
    response = redirect(reverse("books"))
    return response


def books(request):
    """Список книг с поиском по названию и автору"""

    try:
        book_id = int(request.GET.get("book_id"))
    except (ValueError, TypeError):
        book_id = None

    try:
        book_author_id = int(request.GET.get("author_id"))
    except (ValueError, TypeError):
        book_author_id = None

    query = Q()
    if book_id:
        query.add(
            Q(pk=book_id), Q.AND,
        )
    if book_author_id:
        query.add(
            Q(authors__pk=book_author_id), Q.AND,
        )

    books_objects = Book.objects.prefetch_related("authors").filter(query)
    authors_lookup = Author.objects.all()
    books_lookup = Book.objects.all()

    return render(
        request,
        "booklist/books.html",
        {
            "books": books_objects,
            "form": {
                "description": "Здесь вы можете ознакомиться с каталогом книг",
                "author": {
                    "title": "Автор",
                    "objects": authors_lookup,
                    "selected": book_author_id,
                },
                "book": {
                    "title": "Наименование",
                    "objects": books_lookup,
                    "selected": book_id,
                },
            },
        },
    )
