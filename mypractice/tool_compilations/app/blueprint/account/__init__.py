from flask_restful import Api
from flask import Blueprint

from app.blueprint.account import view

account = Blueprint("account", __name__)
account_api = Api(account)
account_api.add_resource(view.Business, '/api/test/business/list')
account_api.add_resource(view.TableInfo, '/api/test/business/table_info')
account_api.add_resource(view.TableDetails, '/api/test/business/details')