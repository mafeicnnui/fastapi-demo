#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/23 9:45
# @Author : ma.fei
# @File : main.py.py
# @Software: PyCharm

import uvicorn
import time
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    print('sleep 5s')
    time.sleep(5)
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)