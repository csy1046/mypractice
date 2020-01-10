from app.blueprint.account import parser as ap
from flask_restful import Resource

from app.common.func import make_resp

class Business(Resource):
    """业务接口
    直接把数据写再代码里到原因是，在无法连接到数据库到时候也
    保证该接口可用
    """
    def get(self):
        data = {
            'list': [
                {
                    'name': '全部',
                    'value': 0,
                    'children': []
                }, {
                    'name': '实物',
                    'value': 1,
                    'children': [
                        {
                            'name': '全部',
                            'value': 0,
                        }, {
                            'name': '商城交易',
                            'value': 1,
                        }, {
                            'name': '供应链交易',
                            'value': 2,
                        }, {
                            'name': '自营业务',
                            'value': 3,
                        }, {
                            'name': '云货架',
                            'value': 4,
                        }, {
                            'name': '家电专区',
                            'value': 5,
                        }, {
                            'name': '无人超市',
                            'value': 6,
                        }, {
                            'name': '网吧',
                            'value': 7,
                        }
                    ]
                }, {
                    'name': '能力',
                    'value': 2,
                    'children': [
                        {
                            'name': '全部',
                            'value': 0
                        }, {
                            'name': '酒店ITV',
                            'value': 2
                        }, {
                            'name': '游戏',
                            'value': 3
                        }, {
                            'name': '家庭ITV',
                            'value': 5
                        }
                    ]
                }
            ]
        }
        return make_resp(data=data)


class TableInfo(Resource):

    def get(self):
        req = ap.table_info.parse_args(strict=True)
        result = [
            {'name': '订单属性信息',
             'table': 'orderInfo',
             'column': [
                 {'name': '订单ID',
                  'column': 'orderId',
                  'control': [1]},
                 {'name': '下单时间',
                  'column': 'orderTime',
                  'control': [2]},
                 {'name': '订单金额',
                  'column': 'orderSum',
                  'control': [2]}
             ]},
            {'name': '商品店铺信息',
             'table': 'shopInfo',
             'column': [
                 {'name': '店铺ID',
                  'column': 'shopId',
                  'control': [1]},
                 {'name': '商品数量',
                  'column': 'goodsNum',
                  'control': [2]},
                 {'name': '订单金额',
                  'column': 'orderSum',
                  'control': [2]}
             ]}
        ]
        return make_resp(data={'list': result, 'total': len(result)})


class TableDetails(Resource):

    def post(self):
        req = ap.table_query.parse_args(strict=True)
        result = [
            {}
        ]
        return result