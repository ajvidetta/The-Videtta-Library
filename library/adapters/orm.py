from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym
from sqlalchemy.exc import ArgumentError

from library.domain import model

# global variable giving access to the MetaData (schema) information of the database
metadata = MetaData()

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)

books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('title', String(255), nullable=False),
    Column('authors', String(512)),
    Column('description', String(4096)),
    Column('average_rating', Integer)
)


def map_model_to_tables():
    try:
        mapper(model.User, users_table, properties={
            '_User__user_name': users_table.c.user_name,
            '_User__password': users_table.c.password,
        })
    except ArgumentError:
        pass

    try:
        mapper(model.Book, books_table, properties={
            '_Book__book_id': books_table.c.id,
            '_Book__title': books_table.c.title,
            '_Book__authors': books_table.c.authors,
            '_Book__description': books_table.c.description,
            '_Book__average_rating': books_table.c.average_rating,

        })
    except ArgumentError:
        pass




