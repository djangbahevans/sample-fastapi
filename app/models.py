from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True, nullable=False)
    title = Column("title", String, nullable=False)
    content = Column("content", String, nullable=False)
    published = Column("published", Boolean,
                       server_default='True', nullable=False)
    created_at = Column("created_at", TIMESTAMP(
        timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    created_at = Column("created_at", TIMESTAMP(
        timezone=True), nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column("post_id", Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
