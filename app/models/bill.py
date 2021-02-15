from datetime import datetime
from typing import Union

from sqlalchemy import Column, String, FLOAT, DateTime

from app.database import db


class Bill(db.Base):
    """Bill table"""
    __tablename__ = "bills"
    uuid: Union[Column, str] = Column(String(16), primary_key=True, unique=True)
    filepath: Union[Column, str] = Column(String(40), nullable=False)
    price: Union[Column, float] = Column(FLOAT, nullable=False)
    date: Union[Column, datetime] = Column(DateTime, nullable=False)
    category: Union[Column, str] = Column(String(20), nullable=False)
    user: Union[Column, str] = Column(String(20), nullable=False)


# db.Base.metadata.create_all(db.engine)

'''cartegories:
freizeit
kleidung
elektronik
essen
'''
