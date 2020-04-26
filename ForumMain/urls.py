# coding:utf-8 
# author:james
# datetime:2020/4/26 20:16
from tornado.web import url, StaticFileHandler

from ForumMain.settings import settings

urlpattern = [
    (url("/media/(.*)", StaticFileHandler, {'path': settings['MEDIA_ROOT']}))
]
