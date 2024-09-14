#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/9/4 14:57
# @Author : ma.fei
# @File : main.py.py
# @Software: PyCharm

import uvicorn
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)