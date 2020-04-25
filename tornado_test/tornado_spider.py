# coding:utf-8 
# author:james
# datetime:2020/4/25 18:20
from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient

base_url = ""

async def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    print(response.body)
    return response.body

if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(lambda:fetch_coroutine("http://www.baidu.com"))