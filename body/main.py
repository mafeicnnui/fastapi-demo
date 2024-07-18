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

'''

import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000/",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/api/")
async def query_item():
    return {"answer":"yes","forced":False,"image":"https://yesno.wtf/assets/yes/8-2f93962e2ab24427df8589131da01a4d.gif"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)