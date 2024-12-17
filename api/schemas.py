from datetime import datetime
from pydantic import BaseModel

class ItemBase(BaseModel):
    name : str
    description : str | None = None
    type_id : int
    score : int
    image_url : str | None = None
    url : str | None = None


class Item(ItemBase):
    date_added : datetime
    id: int
    class Config:
        orm_mode = True
        

class ItemsTypeBase(BaseModel):
    name : str
    

class ItemsType(ItemsTypeBase):
    id : int
    items : list[Item] = []
    class Config:
        orm_mode = True