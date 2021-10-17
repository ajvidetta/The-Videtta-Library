from typing import Iterable
import random

from library.adapters.repository import AbstractRepository
from library.domain.model import Book


def get_book_names(repo: AbstractRepository):
    books = repo.get_books()
    book_titles = [book.title for book in books]

    return book_titles


def sort_books(repo: AbstractRepository):
    books = repo.get_books()
    books = sorted(books)


def get_random_book(repo: AbstractRepository):
    books = repo.get_books()
    return random.choice(books)


def sort_books(repo: AbstractRepository):
    books = repo.sort_books()

    return books


def get_book_by_title(book_title, repo: AbstractRepository):

    book = repo.get_book_by_title(book_title)

    return book

# ============================================
# Functions to convert dicts to model entities and vice versa
# ============================================


def book_to_dict(book: Book):
    try:
        book_dict = {
            'id': book.book_id,
            'description': book.description,
            'title': book.title,
            'authors': book.authors,
        }
        return book_dict
    except AttributeError:
        return book


def dict_to_book(dict):
    book = Book(dict.id, dict.title)
    for i in dict.authors:
        book.add_author(i)
    book.description = dict.description

    return book
