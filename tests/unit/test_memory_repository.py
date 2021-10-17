from datetime import date, datetime
from typing import List

import pytest

from library.domain.model import Publisher, Author, Book, Review, BooksInventory, User

from library.adapters.repository import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', 'mvNNbc1eLA$i')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_add_book(in_memory_repo):
    book = Book(
        111222333,
        "TestBook"
    )
    in_memory_repo.add_book(book)

    assert in_memory_repo.get_book_by_title('TestBook') is book


def test_repository_can_retrieve_all_books(in_memory_repo):
    books = in_memory_repo.get_books()

    # Check that the book list is as expected
    assert len(books) == 245


def test_repository_can_retrieve_book_by_title(in_memory_repo):
    book = in_memory_repo.get_book_by_title("D.Gray-man, Vol. 16: Blood & Chains")

    # Check that the Book has the expected title.
    assert book.title == "D.Gray-man, Vol. 16: Blood & Chains"


def test_repository_can_retrieve_book_by_id(in_memory_repo):
    book = in_memory_repo.get_book_by_id(18955715)

    # Check that the Book has the expected title.
    assert book.title == "D.Gray-man, Vol. 16: Blood & Chains"


def test_repository_does_not_retrieve_a_non_existent_book_title(in_memory_repo):
    book = in_memory_repo.get_book_by_title("the life and lies of albus dumbledoor")

    # Check that the Book has the expected title.
    assert book is None


def test_repository_does_not_retrieve_a_non_existent_book_id(in_memory_repo):
    book = in_memory_repo.get_book_by_id(23)

    # Check that the Book has the expected title.
    assert book is None


def test_repository_can_get_first_book(in_memory_repo):
    book = in_memory_repo.get_first_book()
    assert book.title == '20th Century Boys, Libro 15: ¡Viva la Expo! (20th Century Boys, #15)'


def test_repository_returns_previous_book(in_memory_repo):
    book = in_memory_repo.get_book_by_title("Superman Archives, Vol. 2")
    prev = in_memory_repo.get_name_of_previous_book(book)

    assert prev.title == 'Captain America: Winter Soldier (The Ultimate Graphic Novels Collection: Publication Order, #7)'


def test_repository_returns_none_when_there_are_no_previous_books(in_memory_repo):
    book = in_memory_repo.get_book_by_title("20th Century Boys, Libro 15: ¡Viva la Expo! (20th Century Boys, #15)")
    prev = in_memory_repo.get_name_of_previous_book(book)

    assert prev is None


def test_repository_returns_next_book(in_memory_repo):
    book = in_memory_repo.get_book_by_title("Superman Archives, Vol. 2")
    prev = in_memory_repo.get_name_of_next_book(book)

    assert prev.title == 'The Breaker New Waves, Vol 11'

