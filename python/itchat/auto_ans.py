import itchat
import json
from urllib import request
from itchat.content import *

tuling_key = 'b948081d3b4e485d9af5abd2f83730a8'
api = 'http://www.tuling123.com/openapi/api?key=' + tuling_key + '&info='


def getHtml(req):
    page = request.urlopen(req)
    html = page.read()
    html = html.decode('utf-8')
    return html 

def get_response(msg):
    info = msg
    req = api + info
    res = getHtml(req)
    dic_json = json.loads(res)
    

@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg['FromUserName'] == '@efd311ea496fbfcd5b55ae8a164512845605463d6c5703cab311c0f8b4018f3a':
        return '你是xxxx~'  #可以对某人专门回复
    else:
        return get_response(msg['Text'])

@itchat.msg_register(TEXT, isGroupChat = True)
def text_reply(msg):
    white_list = {
        'group1':'@@6c32580cba11502d126e61dcbdc6ee4e4e07938261e419cfe21782d74d171830',
        'group2':'@@dd80c3d625df785ebb885f4bfc0a0f8f3964b656a1e3f3ed5f4f2949d6eb09e9',
        }
    print(msg['Text'])
    print(msg['FromUserName'])
    if msg['FromUserName'] in white_list.values():
        print('~~~~~~~~~~~~~~~~~')
        return get_response(msg['Text'])




if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run(debug=True)
