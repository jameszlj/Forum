# coding:utf-8 
# author:james
# datetime:2020/4/26 20:11
import tornado.ioloop
from tornado import web

from ForumMain.settings import settings
from ForumMain.urls import urlpattern

if __name__ == '__main__':
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()