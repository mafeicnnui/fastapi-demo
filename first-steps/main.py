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
 https://fastapi.tiangolo.com/zh/project-generation/
 http://127.0.0.1:8000/docs
'''
from fastapi import FastAPI
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
