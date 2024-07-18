#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/10 10:12
# @Author : ma.fei
# @File : database.py
# @Software: PyCharm
# https://blog.adnansiddiqi.me/getting-started-with-fastapi-and-mysql/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus as urlquote


db_config = {
    'user':'puppet',
    'password':urlquote('Puppet@123'),
    'ip':'10.2.39.18',
    'port':'3306',
    'db':'test',
    'charset':'utf8'
}

engine = create_engine(
    'mysql+pymysql://{user}:{password}@{ip}/{db}?charset={charset}'.format(**db_config),
    echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()