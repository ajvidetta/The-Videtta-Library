import csv
from pathlib import Path

from werkzeug.security import generate_password_hash

from library.adapters.repository import AbstractRepository
from library.domain.model import Book, User
from library.adapters.jsondatareader import BooksJSONReader
from library.utilities import utilities


def load_books(data_path: Path, repo: AbstractRepository):

    authors_filename = '{}/book_authors_excerpt.json'.format(data_path)
    books_filename = '{}/comic_books_excerpt.json'.format(data_path)

    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()

    for i in range(len(reader.dataset_of_books)):
        repo.add_book(reader.dataset_of_books[i])


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: Path, repo: AbstractRepository):
    users = dict()

    users_filename = str(Path(data_path) / "users.csv")
    for data_row in read_csv_file(users_filename):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users
