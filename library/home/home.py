from flask import Blueprint, render_template

import library.utilities.utilities as utilities


home_blueprint = Blueprint(
    'home_bp', __name__)

selected_book=utilities.get_random_book()
@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_book=utilities.get_random_book(),
        book_urls=utilities.get_books_and_urls()
    )
