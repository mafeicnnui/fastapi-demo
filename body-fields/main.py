#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/5/24 15:57
# @Author : ma.fei
# @File : main.py.py
# @Software: PyCharm

'''
pip install "fastapi[all]"
FastAPI:
 https://fastapi.tiangolo.com/zh/tutorial/path-params/
 http://127.0.0.1:8000/docs
 uvicorn main:app --reload
'''
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results