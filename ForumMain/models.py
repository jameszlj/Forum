# coding:utf-8 
# author:james
# datetime:2020/4/30 17:22
import datetime

from peewee import Model, DateTimeField
from ForumMain.settings import database


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.datetime.now(), verbose_name="添加时间")

    class Meta:
        database = database
