from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class ItemsTypes(Base):
    __tablename__ = "types"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    items = relationship("Item", back_populates="type")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    score = Column(Integer)
    image_url = Column(String)
    url = Column(String)
    date_added = Column(Date)
    type_id = Column(Integer, ForeignKey("types.id"))
    type = relationship("ItemsTypes", back_populates="items")
    