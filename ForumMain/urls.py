# coding:utf-8 
# author:james
# datetime:2020/4/26 20:16
import os

from tornado.web import url, StaticFileHandler

from ForumMain.settings import settings

urlpattern = [
    (url(r"/(.*)", StaticFileHandler, {"path":settings['template_path'],'default_filename': "index.html"})),
]
