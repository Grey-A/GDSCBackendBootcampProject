from sqlalchemy import Column, Integer, String
from app.config.database import DBBase


class School(DBBase):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    address = Column(String(500), nullable=False)
