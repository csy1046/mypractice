# -*- coding: utf-8 -*-  
import urllib  
import json  
  
def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()  
    return html  
  
if __name__ == '__main__':  
    key = 'b948081d3b4e485d9af5abd2f83730a8'  
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='  
    while True:  
        info = raw_input('我: ')  
        request = api + info  
        response = getHtml(request)  
        dic_json = json.loads(response)  
        print '吴彦祖: '.decode('utf-8') + dic_json['text'] 
