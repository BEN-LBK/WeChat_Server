# -*- coding: UTF-8 -*-
import hashlib
import urllib
import urllib2
import base64
import json
import time

url_preffix = 'https://api.ai.qq.com/fcgi-bin/'


def setParams(array, key, value):
    array[key] = value


def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, urllib.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str)
    return hash_md5.hexdigest().upper()


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}

    def invoke(self, params):
        self.url_data = urllib.urlencode(params)
        req = urllib2.Request(self.url, self.url_data)
        try:
            rsp = urllib2.urlopen(req)
            str_rsp = rsp.read()
            dict_rsp = json.loads(str_rsp)
            return dict_rsp
        except urllib2.URLError, e:
            dict_error = {}
            if hasattr(e, "code"):
                dict_error = {}
                dict_error['ret'] = -1
                dict_error['httpcode'] = e.code
                dict_error['msg'] = "sdk http post err"
                return dict_error
            if hasattr(e, "reason"):
                dict_error['msg'] = 'sdk http post err'
                dict_error['httpcode'] = -1
                dict_error['ret'] = -1
                return dict_error
            else:
                dict_error = {}
                dict_error['ret'] = -1
                dict_error['httpcode'] = -1
                dict_error['msg'] = "system error"
                return dict_error

    # 图片取词
    def getOcrGeneralocr(self, image):
        self.url = url_preffix + 'ocr/ocr_generalocr'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 场景描述
    def gevision_imgtotext(self, image, mediaId='1535646454'):
        self.url = url_preffix + 'vision/vision_imgtotext'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'session_id', mediaId)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 物体识别
    def getvision_objectr(self, image, topk_number=1):
        self.url = url_preffix + 'vision/vision_objectr'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'format', 1)
        setParams(self.data, 'topk', topk_number)  # 返回结果的个数（已按置信度倒排）
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 人脸分析
    def getdetectface(self, image):
        self.url = url_preffix + 'face/face_detectface'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'mode', 0)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 人脸美妆
    def getfacecosmetic(self, image, cosmetic_type=1):
        self.url = url_preffix + 'ptu/ptu_facecosmetic'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'cosmetic', cosmetic_type)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 人脸变妆
    def getfacedecoration(self, image, decoration_type=1):
        self.url = url_preffix + 'ptu/ptu_facedecoration'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'decoration', decoration_type)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 人脸融合
    def getfacemerge(self, image, model =1):
        self.url = url_preffix + 'ptu/ptu_facemerge'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'model', model)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 大头贴
    def getfacesticker(self, image, sticker_type=1):
        self.url = url_preffix + 'ptu/ptu_facesticker'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        setParams(self.data, 'sticker', sticker_type)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 文字翻译
    def getNlpTextTrans(self, text, type):
        self.url = url_preffix + 'nlp/nlp_texttrans'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'text', text)
        setParams(self.data, 'type', type)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 语义解析
    def getNlpWordCom(self, text):
        self.url = url_preffix + 'nlp/nlp_wordcom'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'text', text)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 图片翻译
    def getNlpImageTrans(self, image, mediaId='451454543', source='auto', target='auto'):
        self.url = url_preffix + '/nlp/nlp_imagetranslate'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'session_id', mediaId)
        setParams(self.data, 'scene', 'doc')
        setParams(self.data, 'source', source)
        setParams(self.data, 'target', target)
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    # 语音识字
    def getAaiWxAsrs(self, chunk, speech_id, end_flag, format_id, rate, bits, seq, chunk_len, cont_res):
        self.url = url_preffix + 'aai/aai_wxasrs'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        speech_chunk = base64.b64encode(chunk)
        setParams(self.data, 'speech_chunk', speech_chunk)
        setParams(self.data, 'speech_id', speech_id)
        setParams(self.data, 'end', end_flag)
        setParams(self.data, 'format', format_id)
        setParams(self.data, 'rate', rate)
        setParams(self.data, 'bits', bits)
        setParams(self.data, 'seq', seq)
        setParams(self.data, 'len', chunk_len)
        setParams(self.data, 'cont_res', cont_res)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    '''
    # 语音合成
    def getAaiToTts(self, text, Speech_ID=1, format_ID=3, volume=10, speed=90, aht=20, apc=50):
        self.url = url_preffix + 'aai/aai_tts'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'speaker', Speech_ID) #普通话男声	1  静琪女声	5  欢馨女声	6  碧萱女声	7
        setParams(self.data, 'format', format_ID)  #PCM	1     WAV	 2    MP3	3
        setParams(self.data, 'volume', volume)#合成语音音量，取值范围[-10, 10]，如-10表示音量相对默认值小10dB，0表示默认音量，10表示音量相对默认值大10dB
        setParams(self.data, 'speed', speed)#合成语音语速，默认100  [50, 200]
        setParams(self.data, 'text', text)#待合成文本
        setParams(self.data, 'aht', aht)#合成语音降低/升高半音个数，即改变音高，默认0  [-24, 24]
        setParams(self.data, 'apc', apc)#控制频谱翘曲的程度，改变说话人的音色，默认58  [0, 100]
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)
    '''

    # 语音合成
    def getAaiToTts(self, text, Speech_ID=6, speed=0):
        self.url = url_preffix + 'aai/aai_tta'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'model_type', Speech_ID)  # 女生	0   女生纯英文	1   男生	2    喜道公子	6
        setParams(self.data, 'speed', speed)  # 合成语音语速，0.6倍速	-2   0.8倍速	-1   正常速度	0  1.2倍速	1  1.5倍速	2
        setParams(self.data, 'text', text)  # 待合成文本
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)
