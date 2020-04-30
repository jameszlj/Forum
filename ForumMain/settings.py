# coding:utf-8 
# author:james
# datetime:2020/4/26 20:18
import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "static_path": os.path.join(BASE_DIR, "Forum-html"),
    "static_url_prefix": "/static/",
    "template_path": "template",
    "media_root": os.path.join(BASE_DIR, "media"),
    "SITE_URL": "http://127.0.0.1:8080",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "name": "message",
        "port": 3306,
    },
}

database = peewee_async.MySQLDatabase(settings['db']['db'],
                                      host=settings['db']['host'],
                                      port=settings['db']['port'],
                                      user=settings['db']['user'],
                                      password=settings['db']['password'],
                                      )
