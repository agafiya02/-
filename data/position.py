import sqlalchemy
from flask_login import UserMixin
from data.session import SqlAlchemyBase


class Position(SqlAlchemyBase, UserMixin):
    __tablename__ = 'menu'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
