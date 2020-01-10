import logging

import datetime
import time
import random
import requests
import urllib.parse
import hashlib

from flask import jsonify
from app.extension import bcrypt

from app.common.constant import Code
from app.config import Config


def make_resp(code=Code.SUCCESS, data=None, msg=None):

    res = {
        "code": code,
        "data": data,
    }
    if msg:
        res["msg"] = msg

    return jsonify(res)


def timestamp2datetime(timestamp):
    if timestamp:
        return datetime.datetime.fromtimestamp(timestamp / 1000)
    else:
        return 0


def generate_bint_id():

    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(0, 10000)).zfill(4)


def get_pages_range(total, page, page_size):
    page = int(page)
    pages, last_size = divmod(total, page_size)
    if page - 1 < pages:
        start = (page - 1) * page_size
        end = start + page_size
    else:
        start = pages * page_size
        end = start + last_size
    return start, end


def str2datetime(date_time):
    return datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')


def datetime2str(date_time):
    return date_time.strftime('%Y-%m-%d %H:%M:%S')


def datetime2timestamp(t):
    """

    :type t: datetime.datetime
    """

    return time.mktime(t.timetuple()) * 1000
