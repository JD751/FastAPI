from fastapi import FastAPI,          HTTPException
from pydantic import BaseModel


app=FastAPI()


class Item(BaseModel):
    id: int
    name:str
    description: str
    price: float

db={}

@app.post("/items/")
async def create_item(item:Item):
    db[item.id]=item
    return {'item':item}

@app.get('/')
async def display_items():
    if not db:
        raise HTTPException(status_code=404, detail="No items found")
    return db

@app.delete('/items/delete')

async def delete_item(id:int):
    if id in db:
        del_item= db[id]
        del db[id]
        return {"deleted_item":del_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.put('/items/update')

async def update_item(item:Item):
    if item.id in db:
        db[item.id]=item
        return item
    else:
        raise HTTPException(status_code=404, detail='This item does not exist')






