from urllib import request
import re
import json

response = request.urlopen("http://mobile.weather.com.cn/js/citylist.xml")
page = response.read().decode("utf-8")
provinces = page.split(',')
provinces_str = provinces[0]
provinces_str = provinces_str.replace('<d','@')
provinces_str = provinces_str.replace('/>','@')
provinces_l = provinces_str.split('@')
provinces_list = []
for pro in provinces_l:
    if pro:
       try:
           pro = pro.strip()
           data = pro.split('="')
           tmp = {}
           tmp['province'] = data[-1][:-1] 
           tmp['city'] = data[2][:-4]
           tmp['code'] = data[1][:-4]
           provinces_list.append(tmp)
       except:
           print(data)
           break
pro_list = []
for p in provinces_list:
    if p['code'][0] == '1' and p['code'][1] == '0' and p['code'][2] == '1':
        pro_list.append(p)

with open('city_code','w') as f:
    f.write(json.dumps(pro_list))
    

