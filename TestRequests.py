# -*-coding:UTF-8-*-
import requests,json
r=requests.get('http://www.zhidaow.com')
# r.encoding='utf-8'
print r.encoding
print r.content
    # .decode('ascii').encode('utf-8')