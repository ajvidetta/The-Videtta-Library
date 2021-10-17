from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from library.adapters.repository import AbstractRepository
from library.domain.model import Publisher, Author, Book, Review, BooksInventory, User


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._User__user_name == user_name).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return user

    def add_book(self, book: Book):
        with self._session_cm as scm:
            scm.session.add(book)
            scm.commit()

    def add_author(self, author: Author):
        with self._session_cm as scm:
            scm.session.add(author)
            scm.commit()

    def get_book_by_id(self, id: int) -> Book:
        book = None
        try:
            book = self._session_cm.session.query(Book).filter(Book._Book__id == id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return book

    def get_book_by_title(self, title: str) -> Book:
        book = None
        try:
            book = self._session_cm.session.query(Book).filter(Book._Book__title == title).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return book

    def get_books_by_author(self, target_author: Author) -> List[Author]:
        if target_author is None:
            books = self._session_cm.session.query(Author).all()
            return books
        else:
            # Return articles matching target_author; return an empty list if there are no matches.
            books = self._session_cm.session.query(Book).filter(Book._Book__authors[0] == target_author).all()
            return books

    def get_first_book(self):
        book = self._session_cm.session.query(Book).first()
        return book

    def get_last_book(self):
        book = self._session_cm.session.query(Book).order_by(desc(Book._Book__title)).first()
        return book

    def get_name_of_previous_book(self, book: Book):
        result = None
        prev_book = self._session_cm.session.query(Book).filter(Book._Book__title < book.title).order_by(desc(Book._Book__title)).first()

        if prev_book is not None:
            result = prev_book.title

        return result

    def get_name_of_next_book(self, book: Book):
        result = None
        next_book = self._session_cm.session.query(Book).filter(Book._Book__title > book.title).order_by(asc(Book._Book__title)).first()

        if next_book is not None:
            result = next_book.title

        return result

    def get_books(self) -> List[Book]:
        # books = self._session_cm.session.query(BooksInventory.get_books).all()
        books = self._session_cm.session.execute('SELECT title FROM books').all()
        return books

