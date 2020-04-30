# coding:utf-8 
# author:james
# datetime:2020/4/26 20:18
import os

from tornado.web import StaticFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "static_path": os.path.join(BASE_DIR, "Forum-html"),
    "static_url_prefix": "/static/",
    "template_path": "template",
    "media_root": os.path.join(BASE_DIR, "media"),
    "SITE_URL": "http://127.0.0.1:8080",
}
