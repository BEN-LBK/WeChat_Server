# -*- coding: utf-8 -*-

'''
编码 : aikes
日期 : 20180221
功能 : 验证腾讯openai的api
环境 ：win10+python3.6+opencv3.4+VS2017
'''
import os
import hashlib
import time
import random
import string
import base64
import requests
import cv2
import numpy as np
from urllib import urlencode
import json  # 用于post后得到的字符串到字典的转换

app_key = 'T1Gj1V8hwZmmxgE1'
app_id = '1106866541'

'''
        腾讯openai鉴权签名计算步骤：（摘抄自官网）
            用于计算签名的参数在不同接口之间会有差异，但算法过程固定如下4个步骤。
        1 将<key, value>请求参数对按key进行字典升序排序，得到有序的参数对列表N
        2 将列表N中的参数对按URL键值对的格式拼接成字符串，得到字符串T（如：key1=value1&key2=value2），URL键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8，而不是小写%e8
        3 将应用密钥以app_key为键名，组成URL键值拼接到字符串T末尾，得到字符串S（如：key1=value1&key2=value2&app_key=密钥)
        4 对字符串S进行MD5运算，将得到的MD5值所有字符转换成大写，得到接口请求签名
'''


def get_params(img):  # 鉴权计算并返回请求参数
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效
    time_stamp = str(int(time.time()))
    # 请求随机字符串，用于保证签名不可预测,16代表16位
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    params = {'app_id': app_id,  # 请求包，需要根据不同的任务修改，基本相同
              'image': img,  # 文字类的任务可能是‘text’，由主函数传递进来
              'mode': '0',  # 身份证件类可能是'card_type'
              'time_stamp': time_stamp,  # 时间戳，都一样
              'nonce_str': nonce_str,  # 随机字符串，都一样
              # 'sign':''                      #签名不参与鉴权计算，只是列出来示意
              }

    sort_dict = sorted(params.items(), key=lambda item: item[0], reverse=False)  # 字典排序
    sort_dict.append(('app_key', app_key))  # 尾部添加appkey
    rawtext = urlencode(sort_dict).encode()  # urlencod编码
    sha = hashlib.md5()
    sha.update(rawtext)
    md5text = sha.hexdigest().upper()  # MD5加密计算
    params['sign'] = md5text  # 将签名赋值到sign
    return params  # 返回请求包


def detectface(filename):
    '''
    	# 用python系统读取方法
    	with open(filename, 'rb') as bin_data:
        image_data = bin_data.read()  # 得到API可以识别的字符串
	'''
    # 用opencv读入图片
    frame = cv2.imread(filename)
    nparry_encode = cv2.imencode('.jpg', frame)[1]
    data_encode = np.array(nparry_encode)
    image_data = base64.b64encode(data_encode)  #得到API可以识别的字符串

    params = get_params(image_data)  # 获取鉴权签名并获取请求参数
    url = "https://api.ai.qq.com/fcgi-bin/face/face_detectface"  # 人脸分析
    # 检测给定图片（Image）中的所有人脸（Face）的位置和相应的面部属性。位置包括（x, y, w, h），面部属性包括性别（gender）, 年龄（age）, 表情（expression）, 魅力（beauty）, 眼镜（glass）和姿态（pitch，roll，yaw）
    detectdata = []
    res = requests.post(url, params).json()
    for obj in res['data']['face_list']:
        if obj['gender'] > 50:
            gender = "男"
        else:
            gender = "女"	

        if   obj['expression'] < 10:
            smile = "黯然伤神"
        elif obj['expression'] < 20:
            smile = "半嗔半喜"
        elif obj['expression'] < 30:
            smile = "似笑非笑"
        elif obj['expression'] < 40:
            smile = "笑逐颜开"
        elif obj['expression'] < 60:
            smile = "喜上眉梢"
        elif obj['expression'] < 80:
            smile = "心花怒放"
        else:
            smile = "一笑倾城"

        detectdata.append({
            '性别':	gender,
            '年龄': obj['age'],	  
            '情感': smile,
            '魅力': obj['beauty']
            #'glass'	: obj['glass'] 
        }) 

    	#content = "性别:{}"+"\n年龄:"+str(ages)+"\n表情:"+str(smile)+"\n魅力:"str(beautys)+"\n"
    	#content = "性别:{gender}\n年龄:{ages}\n表情:{smile}\n魅力:{beauty}\n".format(**detectresurt)		   
        #print 'gender: %s\tage   : %s\tsmile : %s\tbeauty: %s' % (obj['gender'],obj['age'],obj['expression'],obj['beauty'])
    #os.remove(filename)
    detectdata = json.dumps(detectdata, encoding='UTF-8', ensure_ascii=False)
    return detectdata

if __name__ == '__main__':
    detectdata = detectface('./image/main007.jpg')
    print type(detectdata)
    print detectdata
    content = detectdata.encode("utf-8")
    content = content.replace('[','').replace(']','').replace('{','').replace('}','\n').replace(',','')
    print type(content)
    print content