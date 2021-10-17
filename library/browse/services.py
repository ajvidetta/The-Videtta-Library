
from library.adapters.repository import AbstractRepository
from library.domain.model import Book


def get_first_book(repo: AbstractRepository):
    book = repo.get_first_book()

    return book_to_dict(book)


def get_last_book(repo: AbstractRepository):
    book = repo.get_first_book()

    return book_to_dict(book)


def get_book_by_title(book, repo: AbstractRepository):

    if type(book) == dict:
        book = repo.get_book_by_title(book['title'])
    elif type(book) == Book:
        book = repo.get_book_by_title(book.title)
    elif type(book) == str:
        book = repo.get_book_by_title(book)
    else:
        raise Exception('strange input type')

    prev_book = next_book = None

    prev_book = repo.get_book_by_title(repo.get_name_of_previous_book(book))
    next_book = repo.get_book_by_title(repo.get_name_of_next_book(book))

    # Convert Articles to dictionary form.
    book_dto = book_to_dict(book)
    prev_book = book_to_dict(prev_book)
    next_book = book_to_dict(next_book)

    return book_dto, prev_book, next_book


def book_to_dict(book: Book):
    try:
        book_dict = {
            'id': book.book_id,
            'description': book.description,
            'title': book.title,
            'authors': book.authors,
            'average_rating': book.average_rating,
        }
        return book_dict
    except AttributeError:
        return book