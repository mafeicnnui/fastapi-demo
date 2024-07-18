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

import uvicorn,os
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    for file in files:
        result = {
            "filename": file.filename,
            "content-type": file.content_type,
            "read": await file.read()
        }
        print('file=',result)
        fn = file.filename
        save_path = f'./files/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        save_file = os.path.join(save_path, fn)
        f = open(save_file, 'wb')
        data = await file.read()
        f.write(data)
        f.close()

    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)