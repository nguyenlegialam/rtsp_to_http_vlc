# type uvicorn test_fastAPI_github:app --reload to run
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse
import threading
import uvicorn
import requests, os, sys, tempfile, subprocess, base64, time


class MyCamID(BaseModel):
    id_nha: str
    id_cam: str


HTTP_PORT = 6064
lock = threading.Lock()
app = FastAPI()


# cam_id
# 9911: cam cổng
# 9912: cam trệt
# 9913: cam tầng 1
# 9914: cam tầng 2
# 9915: cam tầng 3
# 9916: cam tầng 4
# manager = None
url = 'http://127.0.0.1:9911'


# response_class=RedirectResponse
@app.get("/cam", response_class=RedirectResponse)
async def call(data: MyCamID):
    cam_url = "http://127.0.0.1:{}".format(data.id_cam)
    print(data)
    return cam_url


@app.get("/cam/{cam_id}", response_class=RedirectResponse)
async def stream(cam_id: int):
    cam_url = "http://127.0.0.1:{}".format(cam_id)
    return cam_url


@app.get("/")
async def home():
    print('hello')
    return 'Welcome11'


@app.get("/cam-cong", response_class=RedirectResponse)
async def video_feed_cam_cong():
    return "http://127.0.0.1:9911"


# @app.get("/cam-cong", response_class=FileResponse)
# async def video_feed_cam_cong():
#     return FileResponse('cam_cong_vlc.html')


@app.get("/cam-tret", response_class=RedirectResponse)
async def video_feed_cam_tret():
    return "http://127.0.0.1:9912"


@app.get("/cam-tang1", response_class=RedirectResponse)
async def video_feed_cam_tang1():
    return "http://127.0.0.1:9913"


@app.get("/cam-tang2", response_class=RedirectResponse)
async def video_feed_cam_tang2():
    return "http://127.0.0.1:9914"


@app.get("/cam-tang3", response_class=RedirectResponse)
async def video_feed_cam_tang3():
    return "http://127.0.0.1:9915"


@app.get("/cam-tang4", response_class=RedirectResponse)
async def video_feed_cam_tang4():
    return "http://127.0.0.1:9916"


@app.get("/cam-nha", response_class=FileResponse)
async def video_feed_cam_nha():
    return FileResponse('cam_nha_vlc.html')


# check to see if this is the main thread of execution
if __name__ == '__main__':
    # start the flask app
    uvicorn.run(app, host="0.0.0.0", port=HTTP_PORT, access_log=False)
