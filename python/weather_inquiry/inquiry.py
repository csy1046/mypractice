import json
from urllib import request



URL = 'http://www.weather.com.cn/data/cityinfo/%d.html'
with open('city_code', 'r') as f:
    f = f.read()
def query_all(URL):
    code_list = json.loads(f)
    for code in code_list:
        try:
            url = URL % int(code['code'])
            response = request.urlopen(url)
            page = response.read()
            page = page.decode('utf-8')
            page = json.loads(page)
            code['temp1'] = page['weatherinfo']['temp1']
            code['temp2'] = page['weatherinfo']['temp2']
            code['weather'] = page['weatherinfo']['weather']
            code['ptime'] = page['weatherinfo']['ptime']
        except KeyError:
            code['temp1'] = ''
            code['temp2'] = ''
            code['weather'] = ''
            code['ptime'] = ''
    return code_list

all_data = query_all(URL)
with open('all_weather','w') as f:
    f.write(json.dumps(all_data))

