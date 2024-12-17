from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/types/", response_model=list[schemas.ItemsType])
def get_types(db: Session = Depends(get_db)):
    return crud.get_types(db=db)


@app.get("/type/{type_name}", response_model=schemas.ItemsType)
def get_type_by_name(type_name: str, db: Session = Depends(get_db)):
    return crud.get_type_by_name(type_name=type_name, db=db)


@app.post("/type/", response_model=schemas.ItemsType)
def create_type(type: schemas.ItemsTypeBase, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db=db ,type_name=type.name)
    if db_type:
        raise HTTPException(status_code=400, detail="type already registered")
    return crud.create_type(db=db, type=type)


@app.delete("/item/{item_id}")
def delete_item(item_id: int, db:Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id) 


@app.get("/{type_id}/items/", response_model=list[schemas.Item])
def items_by_type(type_id: int, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items_by_type(type_id=type_id, db=db, limit=limit)
    return items


@app.get("/item/{item_name}", response_model=schemas.Item)
def read_item(item_name: str, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_name(db, item_name=item_name)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post("/item/", response_model=schemas.ItemBase)
def create_item(item: schemas.ItemBase, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_name(db, item_name=item.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered")
    
    return crud.create_item(db=db, item=item)