# -*- coding: UTF-8 -*-
# @Time    : 2018/6/1 
# @Author  : BEN-LK
# @File    : TencentAI_API.py
# @Software: PyCharm

import hashlib
import os
import apiutil
import base64
import random

app_key = 'T1Gj1V8hwZmmxgE1'
app_id = '1106866541'


# 图片取词
def Get_Ocr_GeneralOcr_api(image_name):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getOcrGeneralocr(image_data)

    data_list = []
    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            data_list.append(i['itemstring'])
    return data_list


# 场景描述
def Get_vision_ImgageToText_api(image_name, mediaId='1535646454'):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.gevision_imgtotext(image_data, mediaId)
    text_string = ''
    if rsp['ret'] == 0:
        text_string = rsp['data']['text']
    return text_string


# 物体识别
def Get_vision_objectr_api(image_name, topk_number=1):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getvision_objectr(image_data, topk_number)  # 返回结果个数（已按置信度倒排）
    data_lists = []
    if rsp['ret'] == 0:
        for obj in rsp['data']['object_list']:
            data_list = [str(obj['label_id']), str(obj['label_confd'])]
            data_lists.append(data_list)
    return data_lists


# 人脸分析
def Get_face_detectface_api(image_name):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getdetectface(image_data)
    detect_data_dict = []
    if rsp['ret'] == 0:
        for obj in rsp['data']['face_list']:
            if obj['gender'] > 50:
                gender = "男"
            else:
                gender = "女"

            if obj['expression'] < 10:
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

            detect_data_dict.append({
                '性别': gender,
                '年龄': obj['age'],
                '情感': smile,
                '魅力': obj['beauty']
            })
    return detect_data_dict


# 人脸美妆
def Get_face_cosmetic_api(image_name, mediaId, cosmetic_type=random.randint(1, 23)):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()  # 原始图片的base64编码数据（原图大小上限500KB)

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getfacecosmetic(image_data, cosmetic_type)
    image_file_name = "./image/%s_x.jpg" % mediaId
    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file_image = open(image_file_name, 'wb')
        file_image.write(imgdata)
        file_image.close()
    return image_file_name


# 人脸变妆
def Get_face_decoration_api(image_name, mediaId, cosmetic_type=random.randint(1, 22)):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()  # 原始图片的base64编码数据（原图大小上限500KB)

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getfacedecoration(image_data, cosmetic_type)
    image_file_name = "./image/%s_b.jpg" % mediaId
    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file_image = open(image_file_name, 'wb')
        file_image.write(imgdata)
        file_image.close()
    return image_file_name


# 人脸融合
def Get_face_merge_api(image_name, mediaId, model=random.randint(1, 50)):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()  # 原始图片的base64编码数据（原图大小上限500KB)

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getfacemerge(image_data, model)
    image_file_name = "./image/%s_m.jpg" % mediaId
    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file_image = open(image_file_name, 'wb')
        file_image.write(imgdata)
        file_image.close()
    return image_file_name


# 大头贴
def Get_face_sticker_api(image_name, mediaId, model=random.randint(1, 31)):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()  # 原始图片的base64编码数据（原图大小上限500KB)

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getfacesticker(image_data, model)
    image_file_name = "./image/%s_s.jpg" % mediaId
    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file_image = open(image_file_name, 'wb')
        file_image.write(imgdata)
        file_image.close()
    return image_file_name

# 文字翻译
def Get_Nlp_TextTrans_api(str_text, type=0):
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getNlpTextTrans(str_text, type)
    data_string = ''
    if rsp['ret'] == 0:
        data_string = rsp['data']['trans_text']
    return data_string


# 语义解析
def Get_Nlp_WordCom_api(str_text):
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getNlpWordCom(str_text)
    data_list = []
    if rsp['ret'] == 0:
        intent_dict = {'intent': rsp['data']['intent']}
        data_list.append(intent_dict)
        for obj in rsp['data']['com_tokens']:
            if obj['com_type'] < 50:
                data_list.append(obj)
    return data_list


# 图片翻译
def Get_Nlp_ImageTrans_api(image_name, mediaId='451454543', source='auto', target='auto'):
    with open(image_name, 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getNlpImageTrans(image_data, mediaId, source, target)
    data_lists = []
    if rsp['ret'] == 0:
        for obj in rsp['data']['image_records']:
            data_list = [obj['source_text'], obj['target_text']]
            data_lists.append(data_list)
    return data_lists


# 语音识字
def get_Aai_WxAsrs_api(file_path, for_mat=8, rate=16000, bits=16, seq=0, cont_res=1):
    once_size = 6400
    f = open(file_path, 'r')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    speech_id = str(hash).upper()
    f.close()
    f = open(file_path, 'rb')
    file_size = os.path.getsize(file_path)
    data_list = []
    try:
        while True:
            chunk = f.read(once_size)
            if not chunk:
                break
            else:
                chunk_size = len(chunk)
                if (seq + chunk_size) == file_size:
                    end = 1
                else:
                    end = 0
            ai_obj = apiutil.AiPlat(app_id, app_key)
            rsp = ai_obj.getAaiWxAsrs(chunk, speech_id, end, for_mat, rate, bits, seq, chunk_size, cont_res)
            seq += chunk_size
            if rsp['ret'] == 0:
                data_list.append(rsp['data']['speech_text'])
        return data_list
    finally:
        f.close()


# 语音合成
def get_Aai_ToTts_api(str_text, mediaId='451454543', Speech_ID=6, speed=0):
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getAaiToTts(str_text, Speech_ID, speed)  # 普通话男声	1  静琪女声	5  欢馨女声	6  欢馨女声	6
    if rsp['ret'] == 0:
        str_data = rsp['data']['voice']
        speech_chunk = base64.b64decode(str_data)
        file_name = './data/%s.mp3' % mediaId
        file_data = open(file_name, 'wb')
        file_data.write(speech_chunk)
        file_data.close()
    return file_name


if __name__ == '__main__':
    pass
    str_text = '在饭店和女朋友提分手，她伤心的哭了'
    data_list = Get_Nlp_WordCom_api(str_text)
    #print data_list
    print "意图", data_list[0]['intent']
    for obj in data_list[1:]:
        print "%s%s%s" % (obj['com_type'], ':', obj['com_word'])
    """
# 语音合成
    #str_text = '在饭店和女朋友提分手，她伤心的哭了。在场的所有人都以为我在求婚——于是掌声响了起来.'
    str_text = '哈喽!我是迪森,你可以用文字或者语音和我聊天,也可以发给我图片,我给你分析美化一下。' #UTF-8编码，非空且长度上限150字节
    file_voice = get_Aai_ToTts_api(str_text,"hello")

    print file_voice
    """

    """
# 语音识字
    data =  get_Aai_WxAsrs_api()
    #for obj in data:
    print data[-1]
    """

    """
# 图片翻译
    image_name = '../data/generalocr.jpg'
    image_data = Get_Nlp_ImageTrans_api(image_name)
    for obj in image_data:
        print "源文本：",obj[0]
        print "译文本：",obj[1]
    """

    """
# 文字翻译
    str_text = '今天天气怎么样'
    data = Get_Nlp_TextTrans_api(str_text)
    print data
    """

    """
# 人脸融合
    image_name = '../data/f-4.jpg'
    image_name = Get_face_merge_api(image_name, 'merge',25)
    print image_name
    """

    """
# 人脸变妆
    image_name = '../data/f-5.jpg'
    image_name = Get_face_decoration_api(image_name, 'fsdgf')
    print image_name
    """

    """
# 人脸美妆
    image_name = '../data/f-5.jpg'
    image_name = Get_face_cosmetic_api(image_name, 'fsdgf')
    print image_name
    """

    """
# 大头贴
    image_name = '../data/f-5.jpg'
    image_name = Get_face_sticker_api(image_name, 'fsdgf')
    print image_name
    """

    """
# 人脸分析
    image_name = '../data/f-7.jpg'
    image_data = Get_face_detectface_api(image_name)
    for obj in image_data:
        for inf in obj.items():
            print inf[0], ":", inf[1]
    """

    """
# 物体识别
    image_name = '../data/place-4.jpg'
    image_data = Get_vision_objectr_api(image_name, 2)
    print image_data
    """

    """
 场景描述
    image_name = '../data/place-4.jpg'
    image_data = Get_vision_ImgageToText_api(image_name,'dsklanvlkasdd')
    print image_data
    """

    """
# 图片取词
    image_name = '../data/generalocr.jpg'
    image_data = Get_Ocr_GeneralOcr_api(image_name)
    for obj in image_data:
        print obj
    """
