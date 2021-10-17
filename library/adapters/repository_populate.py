from pathlib import Path

from library.adapters.repository import AbstractRepository
from library.adapters.data_importer import load_users, load_books


def populate(data_path: Path, repo: AbstractRepository, database_mode: bool):
    # Load users into the repository.
    load_users(data_path, repo)
    # Load books into the repository.
    load_books(data_path, repo)  # , database_mode



