# coding:utf-8 
# author:james
# datetime:2020/4/26 20:18
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    "static_path": os.path.join(BASE_DIR,"static"),
    "template_path": os.path.join(BASE_DIR,"templates"),
}
