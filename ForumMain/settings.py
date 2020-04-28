# coding:utf-8 
# author:james
# datetime:2020/4/26 20:18
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    "static_path": os.path.join(BASE_DIR, "static"),
    "static_url_prefix": "/static",
    "template_path": os.path.join(BASE_DIR, "templates"),
    # custom
    "media_root": os.path.join(BASE_DIR, "media"),
    "site_url": os.environ.get("SITE_URL", "http://127.0.0.1:8080"),
}
