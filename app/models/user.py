from typing import Union

from sqlalchemy import Boolean, Column, String

from app.database import db


class User(db.Base):
    """User table"""
    __tablename__ = "users"

    name: Union[Column, str] = Column(String(20), primary_key=True, unique=True)
    password: Union[Column, str] = Column(String(60), nullable=False)
    active: Union[Column, bool] = Column(Boolean, default=False)

#db.Base.metadata.create_all(db.engine)
