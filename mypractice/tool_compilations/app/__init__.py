# -*- coding = utf-8 -*-
import datetime
import decimal
import logging
import time
from json import JSONEncoder
from flask import session, g
from flask import Flask, request
from flask_login import AnonymousUserMixin, current_user, logout_user
from mongoengine import register_connection
from app.database import db_session as sb

from app.config import Config
from app.extension import apscheduler

def create_app():
    application = Flask(Config.PROJECT, template_folder="dist")

    config_app(application)
    config_logging()
    config_mongodb()
    config_blueprint(application)
    config_request(application)
    config_aps(application)

    # config_app(application)
    @application.teardown_appcontext
    def shutdown_session(response_or_exc):
        try:
            sb.commit()
        except Exception as e:
            # logging.exception(e)
            pass
        finally:
            sb.remove()
        return response_or_exc

    return application


def config_app(application):
    """

    :type application: Flask
    """

    application.config.from_object(Config)

    class CustomJSONEncoder(JSONEncoder):

        def default(self, o):

            if isinstance(o, decimal.Decimal):
                res = str(o)
                return res
            if isinstance(o, datetime.datetime):
                return time.mktime(o.timetuple()) * 1000

            return super(CustomJSONEncoder, self).default(o)

    application.json_encoder = CustomJSONEncoder


def config_mongodb():
    register_connection("default",
                        host=Config.MONGODB_HOST,
                        connect=False)




def config_logging():
    pass


def config_blueprint(application):
    """

    :type application: Flask
    """

    from app.blueprint.account import account
    application.register_blueprint(account)
    from app.blueprint.frontend import frontend
    application.register_blueprint(frontend)

    # 异常页面处理
    from app.blueprint.frontend.view import not_found_handler, server_error
    application.register_error_handler(404, not_found_handler)
    application.register_error_handler(500, server_error)

    # def custom_abort(status_code, *args, **kwargs):
    #     if status_code == 400:
    #         abort(make_result(code=Code.INVALID_PARAMS))
    #     elif status_code == 500:
    #         abort(make_result(code=Code.SYSTEM_ERROR))
    #     else:
    #         abort(status_code)
    #
    # flask_restful.abort = custom_abort




def config_request(app):
    @app.before_request
    def l():
        try:
            g.is_duplicate_removal = current_user.is_duplicate_removal
        except Exception:
            g.is_duplicate_removal = 1


def config_aps(app):
    apscheduler.init_app(app)
    apscheduler.start()
