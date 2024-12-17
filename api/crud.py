from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_item_by_name(db: Session, item_name:str):
    return db.query(models.Item).filter(models.Item.name.like(f"%{item_name}%")).first()


def get_items_by_type(db: Session, type_id:int, limit: int = 100):
    return db.query(models.Item).filter(models.Item.type_id == type_id).limit(limit).all()


def create_item(db: Session, item: schemas.ItemBase):
    db_item = models.Item(**item.model_dump(), date_added=datetime.today())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    item = db.get(models.Item, item_id)
    db.delete(item)
    db.commit()
    return f'{item["name"]} was DELETED'


# ======= TYPES =========
def get_types(db:Session):
    return db.query(models.ItemsTypes).all()


def get_type_by_name(db: Session, type_name: str):
    return db.query(models.ItemsTypes).filter(models.ItemsTypes.name == type_name).first()


def create_type(db:Session, type: schemas.ItemsTypeBase):
    db_item = models.ItemsTypes(**type.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item