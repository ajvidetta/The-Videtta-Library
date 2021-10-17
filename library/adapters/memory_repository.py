import csv
from pathlib import Path
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from library.adapters.repository import AbstractRepository
from library.domain.model import Publisher, Author, Book, Review, BooksInventory, User


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__books = list()
        self.__authors = list()
        self.__users = list()

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def get_books(self):
        return self.__books

    def get_book_by_title(self, name) -> Book:
        return next((book for book in self.__books if book.title == name), None)

    def get_book_by_id(self, id_) -> Book:
        return next((book for book in self.__books if book.book_id == id_), None)

    def get_books_by_author(self, author: Author) -> List[Book]:
        matching_books = list()

        try:
            for book in self.__books:
                if author in book.authors:
                    matching_books.append(book)
                else:
                    break
        except ValueError:
            # No books for specified author. Simply return an empty list.
            pass

        return matching_books

    def add_book(self, book: Book):
        if len(self.__books) == 0:
            self.__books.append(book)
        else:
            for i in range(len(self.__books)):
                if book.title < self.__books[i].title:
                    if i == 0:
                        self.__books.insert(0, book)
                    else:
                        self.__books.insert(i-1, book)

        # self.__books.append(book)

    def add_author(self, author: Author):
        self.__authors.append(author)

    def get_first_book(self):
        book = None

        if len(self.__books) > 0:
            book = self.__books[0]
        return book

    def get_last_book(self):
        book = None

        if len(self.__books) > 0:
            book = self.__books[-1]
        return book

    def get_name_of_previous_book(self, book: Book):

        prev_book = None
        if self.__books.index(book) == 0:
            return prev_book
        else:
            return self.__books[self.__books.index(book) - 1]

    def get_name_of_next_book(self, book: Book):
        next_book = None
        if self.__books.index(book) == len(self.__books) - 1:
            return next_book
        else:
            return self.__books[self.__books.index(book) + 1]
