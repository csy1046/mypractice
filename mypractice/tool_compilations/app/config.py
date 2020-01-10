# -*- coding = utf-8 -*-
import os

from apscheduler.jobstores.mongodb import MongoDBJobStore


class Config:
    PROJECT = 'tyfo_tools'
    MONGODB_HOST = 'mongodb://10.0.0.62/pope'

    timezone = 'Asia/Shanghai',

    SECRET_KEY = "6asCW!GkCjg87$lc123"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://hive:v8Gwtql0erCNw9ip@10.0.0.62/qa_tyfo_data"
    )
    SQLALCHEMY_MAX_OVERFLOW = os.environ.get("SQLALCHEMY_MAX_OVERFLOW", 20)
    SQLALCHEMY_POOL_RECYCLE = os.environ.get("SQLALCHEMY_POOL_RECYCLE", 60)
    SQLALCHEMY_POOL_SIZE = os.environ.get("SQLALCHEMY_POOL_SIZE", 100)

