#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/10 10:12
# @Author : ma.fei
# @File : models.py
# @Software: PyCharm

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_database.sql_app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(50),unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    description = Column(String(200), index=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")