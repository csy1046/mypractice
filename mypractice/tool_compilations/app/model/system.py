# -*- coding = utf-8 -*-

import hashlib
import logging
from datetime import datetime
from mongoengine import DynamicDocument, StringField, DateTimeField, \
    ReferenceField, IntField, ListField, SequenceField, BooleanField, DictField

from app.config import Config
from app.extension import bcrypt


class SystemArea(DynamicDocument):
    """从数据库中获取省市县信息"""
    id = IntField(default=0)
    name = StringField(default='')
    level = IntField(default=0)
    father_id = IntField(default=0)


class LogonUser(DynamicDocument):
    # 用户id
    uid = IntField(default=0)
    # 登录时间
    logon_time = IntField(default=0)
    # 员工姓名
    name = StringField(default='')
    # 用户名
    username = StringField(default='')


class AccessRecord(DynamicDocument):
    # 用户 id
    uid = IntField(default='')
    # 访问路径
    path = ListField()
    # 访问时刻
    time = IntField()
    # 应用标识
    app_id = IntField(default=0)
    # 访问 id
    access_id = StringField(default='')
    # 登录时间
    logon_time = IntField(default=0)
    # 员工姓名
    name = StringField(default='')
    # 用户名
    username = StringField(default='')
