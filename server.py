# coding:utf-8 
# author:james
# datetime:2020/4/26 20:11
import tornado.ioloop
from tornado import web
from tornado.options import define, options

from ForumMain.settings import settings
from ForumMain.urls import urlpattern
define("port", default=8080, help="run on the given port ", type=int)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()