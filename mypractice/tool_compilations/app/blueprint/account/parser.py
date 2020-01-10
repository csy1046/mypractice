from flask_restful.reqparse import RequestParser

def date_parser(data):
    try:
        data = int(data)
    except (TypeError, ValueError):
        raise TypeError("Date must be Int")
    if data == -1:
        return data
    return int(data / 1000)

table_info = RequestParser()
table_info.add_argument('type', location="args", type=int, required=True)

table_query = RequestParser()
table_query.add_argument('page', location='json', type=int)
table_query.add_argument('count', location='json', type=int)
table_query.add_argument('metric', location='json', type=int, required=True)
table_query.add_argument('period', location='json', type=int, required=True)
table_query.add_argument('start', location='json', type=date_parser, required=True)
table_query.add_argument('end', location='json', type=date_parser, required=True)
table_query.add_argument('sort', location='json', type=int, required=True)
table_query.add_argument('sortType', location='json', type=str, required=True)
table_query.add_argument('search', location='json', type=dict, action='append', required=True)
