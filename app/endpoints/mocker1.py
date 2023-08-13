#coding:utf-8

import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

app = APIRouter()

@app.route(path="/api/users")
async def mymock(request_method: str):
    mockjson = '{"msg": "mock成功！"}'
    return JSONResponse(status_code=200, content=json.loads(mockjson))
