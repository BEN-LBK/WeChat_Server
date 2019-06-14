# -*- coding: utf-8 -*-
import requests


'''
def talks_robot(info = '你叫什么名字'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '450b9ca342d54aabbb9dd1c6428b7def'
    data = {'key': apikey,
        'info': info}
    print data
    req = requests.post(api_url, data=data).text
    print req
    replys = json.loads(req)['text']
    print replys
    return replys 
'''


def talks_robot(userid, content='你叫什么名字'):
    url = 'http://www.tuling123.com/openapi/api'
    data_packet = {"key": "450b9ca342d54aabbb9dd1c6428b7def", "info": content, "userid": userid}
    result = requests.post(url, data=data_packet)
    print result
    j = eval(result.text)
    code = j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text'] + j['url']
    elif code == 302000:
        recontent = j['text'] + j['list'][0]['info'] + j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text'] + j['list'][0]['info'] + j['list'][0]['detailurl']
    else:
        recontent = '这货还没学会怎么回复这句话'
    return recontent
