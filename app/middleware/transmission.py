import httpx

from fastapi import Request, Response
from app.config import *
from fastapi import FastAPI

from utils.logger import logger

app = FastAPI()


@app.middleware("http")
async def path_matching_middleware(request: Request, call_next):
    global skucache
    # 获取当前请求的路径
    current_path = request.url.path

    # 检查路径是否被mock
    if current_path not in matched_paths:
        target_url = raw_url + request.url.path
        if request.url.query:
            target_url += '?' + request.url.query
        logger.info(f'Redirect to: {target_url}')
        newheaders = dict(request.headers)

        to_del_header = ['x-real-ip','x-forwarded-for','x-forwarded-proto']
        for h in to_del_header:
            if h in newheaders.keys():
                del newheaders[h]

        newheaders['host'] = raw_host if raw_host else newheaders['host']


        #async with httpx.AsyncClient(verify=False,proxies='http://127.0.0.1:8080') as client:
        async with httpx.AsyncClient(verify=False, proxies=None) as client:
            response = await client.request(request.method, target_url, headers=newheaders,data=await request.body())

            # 判断状态码是否是301 302
            if response.status_code in [301,302]:
                # 获取重定向的URL
                redirect_url = response.headers['location']
                # 发送新的请求到重定向的URL
                response = await client.request(request.method, redirect_url, headers=newheaders,data=await request.body())

            return Response(content=response.content, status_code=response.status_code,headers=response.headers)

    # continue handle request
    response = await call_next(request)
    return response