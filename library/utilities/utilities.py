from flask import Blueprint, request, render_template, redirect, url_for, session

import library.adapters.repository as repo
import library.utilities.services as services


# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


def get_books_and_urls():
    book_names = services.get_book_names(repo.repo_instance)
    book_urls = dict()
    for book_name in book_names:
        book_urls[book_name] = url_for('browse_bp.browse_by_title', tag=book_name)

    return book_urls


def sort_books():
    book = services.sort_books(repo.repo_instance)
    book = services.get_book_by_title(book[0], repo.repo_instance)
    return book


def get_random_book():
    book = services.get_random_book(repo.repo_instance)
    # book['hyperlink'] = url_for('browse_bp.browse')
    book = services.get_book_by_title(book[0], repo.repo_instance)
    return book
