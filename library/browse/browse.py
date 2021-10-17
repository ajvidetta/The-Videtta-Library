from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from library.domain.model import Book

import library.adapters.repository as repo
import library.utilities.utilities as utilities
import library.browse.services as services


browse_blueprint = Blueprint(
    'browse_bp', __name__)


@browse_blueprint.route('/browse_by_title', methods=['GET'])
def browse_by_title():
    target_book = request.args.get('title')

    first_book = services.get_first_book(repo.repo_instance)
    last_book = services.get_last_book(repo.repo_instance)

    if target_book is None:
        target_book = services.get_first_book(repo.repo_instance)

    book, prev_book, next_book = services.get_book_by_title(target_book, repo.repo_instance)

    next_book_url = None
    prev_book_url = None

    if prev_book is not None:
        # There are articles on a previous date, so generate URLs for the 'previous' and 'first' navigation buttons.
        if type(prev_book) == dict:
            prev_book_url = url_for('browse_bp.browse_by_title', title=prev_book['title'])
        if type(prev_book) == Book:
            prev_book_url = url_for('browse_bp.browse_by_title', title=prev_book.title)

    # There are articles on a subsequent date, so generate URLs for the 'next' and 'last' navigation buttons.
    if next_book is not None:
        if type(next_book) == dict:
            next_book_url = url_for('browse_bp.browse_by_title', title=next_book['title'])
        if type(next_book) == Book:
            next_book_url = url_for('browse_bp.browse_by_title', title=next_book.title)

    if type(target_book) == dict:
        target_book = target_book['title'] # was like .title
    if type(target_book) == Book:
        target_book = target_book.title

    return render_template(
        'browse/browse.html',
        title=target_book,
        selected_book=book,
        prev_book_url=prev_book_url,
        next_book_url=next_book_url
    )
