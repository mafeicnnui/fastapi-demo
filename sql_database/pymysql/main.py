#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/18 9:52
# @Author : ma.fei
# @File : main.py.py
# @Software: PyCharm

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from urllib.parse import quote_plus as urlquote

db_config = {
    'user':'puppet',
    'password':urlquote('Puppet@123'),
    'ip':'10.2.39.18',
    'port':'3306',
    'db':'test',
    'charset':'utf8'
}

Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://{user}:{password}@{ip}/{db}?charset={charset}'.format(**db_config),
    echo=True)


@contextmanager
def sessionScope():
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String(20))


def find(session):
    result = session.query(Users).filter(Users.name == 'hehe').all()
    print('query result:', result)
    for u in result:
        print('u:', u.email)


def add(session):
    user = Users()
    user.name = '啥东西'
    user.email = '800l@qq.com'
    session.add(user)

if __name__ == '__main__':
    #Base.metadata.create_all(engine)
    with sessionScope() as session:
        add(session)
        find(session)