#coding:utf-8
#fastapi version: 0.101.0
import os

import app.endpoints
from app.endpoints import mocker1
from app.middleware.transmission import *

app = FastAPI()


@app.get("/healthcheck")
async def root():
    return {"message": "OK, I am healthy! 运行正常。"}

@app.on_event("startup")
async def startup_event():
    print('start...')
    print(f'mock api list: ')
    for route in app.routes:
        if hasattr(route, "path"):
            matched_paths.append(route.path)
            print(route.path)

app.middleware("http")(path_matching_middleware)
app.include_router(mocker1.app,prefix='', tags=['mocker'])




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="0.0.0.0", port=443, log_level="info",ssl_keyfile="./sslfile/self-signed.key",ssl_certfile="./sslfile/self-signed.crt", workers=2)