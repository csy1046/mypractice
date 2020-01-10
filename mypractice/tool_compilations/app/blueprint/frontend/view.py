# -*- coding = utf-8 -*-
import logging

from flask.views import MethodView
from flask import render_template, request, url_for, redirect
from flask_login import current_user

class IndexView(MethodView):

    def get(self, *args, **kwargs):

        return render_template("index.html")


def not_found_handler(e):
    logging.exception(e)

    # TODO 404处理

    return "找不到了"


def server_error(e):
    logging.exception(e)

    # TODO 500处理

    return "出错了"
