from sqlalchemy.orm import Session
from src.data import models
from src import schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_all_items(db: Session):
    return db.query(models.Item).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: models.Item, item_update: schemas.ItemUpdate):
    item.name = item_update.name
    item.description = item_update.description
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item: models.Item):
    db.delete(item)
    db.commit()
