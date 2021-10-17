import abc
from typing import List

from library.domain.model import Publisher, Author, Book, Review, BooksInventory, User

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    def add_book(self, book: Book):

        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name) -> User:
        """ Returns the User named user_name from the repository.

        If there is no User with the given user_name, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_books(self) -> List[Book]:
        """ Returns the Book named title from the repository
        If there is no Book with the given title, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_book_by_title(self, title) -> Book:
        """ Returns the Book named title from the repository
        If there is no Book with the given title, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_book_by_id(self, id) -> Book:
        """ Returns the Book identified by id from the repository
        If there is no Book with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_books_by_author(self, author: Author) -> List[Book]:
        """ Returns a list of BookS that were written by author.

        If there are no Books written by author, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_book(self) -> Book:
        """ Returns the first Article, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_book(self) -> Book:
        """ Returns the last Article, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_name_of_previous_book(self, book: Book) -> Book:
        """ Returns the date of an Article that immediately precedes article.

        If article is the first Article in the repository, this method returns None because there are no Articles
        on a previous date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_name_of_next_book(self, book: Book) -> Book:
        """ Returns the date of an Article that immediately follows article.

        If article is the last Article in the repository, this method returns None because there are no Articles
        on a later date.
        """
        raise NotImplementedError

