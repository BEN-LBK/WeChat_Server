# -*- coding: utf-8 -*-
# filename: handle.py

from api import *
from platform import *

import hashlib
import random
import web
import os


# import image_rec


class Handle(object):

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "Hello, What are you nong sha lei ? ? ?"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "madisonLBK"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode:%s, signature:%s " % (hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            #print "\n\nHandle Post webdata is :\n", webData  # 后台打印日志
            recMsg = receive.parse_xml(webData)
            random.seed()
            print "from:  %s \t MsgType:  %s" % (recMsg.FromUserName, recMsg.MsgType)

            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            text_name = "./data/%s.txt" % toUser
            #print text_name
            userid = toUser[0:15]
            if isinstance(recMsg, receive.Msg):

                if recMsg.MsgType == 'text':
                    # content = "text"
                    print "A: ", recMsg.Content
                    retest = talk_api.talks_robot(userid, recMsg.Content)
                    if len(retest) > 1993:
                        content = retest[:1993] + "......"
                    else:
                        content = retest
                    print "B: ", content
                    # content = "：)  " + recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()

                elif recMsg.MsgType == 'image':

                    try:
                        reply.Msg().send()
                        mediaId = recMsg.MediaId
                        myMedia = media.Media()
                        accessToken = basic.Basic().get_access_token()
                        image_name = myMedia.get(accessToken, mediaId)
                        #print image_name
                        content = ''

                        if os.path.exists(text_name):
                            #print 'text_name exists'
                            img_file = open(text_name)
                            str_data = img_file.read(4)
                            #print str_data
                            img_file.close()
                            os.remove(text_name)

                            if str_data == 'fcos':  # "人脸美妆"
                                image_name = TencentAI_API.Get_face_cosmetic_api(image_name, mediaId,random.randint(1, 23))
                                #print image_name
                                print 'cosmetic:done'
                                data_dict = myMedia.uplaod(accessToken, image_name, "image")
                                replyMsg = reply.ImageMsg(toUser, fromUser, data_dict['media_id'])
                                return replyMsg.send()
                            if str_data == 'fdec':  # "人脸变妆"
                                image_name = TencentAI_API.Get_face_decoration_api(image_name, mediaId,random.randint(1, 22))
                                #print image_name
                                print 'decoration:done'
                                data_dict = myMedia.uplaod(accessToken, image_name, "image")
                                replyMsg = reply.ImageMsg(toUser, fromUser, data_dict['media_id'])
                                return replyMsg.send()
                            if str_data == 'fmer':  # "人脸融合"
                                image_name = TencentAI_API.Get_face_merge_api(image_name, mediaId,random.randint(1, 50))
                                #print image_name
                                print 'merge:done'
                                data_dict = myMedia.uplaod(accessToken, image_name, "image")
                                replyMsg = reply.ImageMsg(toUser, fromUser, data_dict['media_id'])
                                return replyMsg.send()
                            if str_data == 'fsti':  # "大头贴"
                                image_name = TencentAI_API.Get_face_sticker_api(image_name, mediaId,random.randint(1, 23))
                                #print image_name
                                print 'sticker:done'
                                data_dict = myMedia.uplaod(accessToken, image_name, "image")
                                replyMsg = reply.ImageMsg(toUser, fromUser, data_dict['media_id'])
                                return replyMsg.send()
                        else:
                            image_data = TencentAI_API.Get_face_detectface_api(image_name)
                            if len(str(image_data)) > 10:
                                # 人脸分析
                                for obj in image_data:
                                    if obj['年龄'] < 30:
                                        content += "这位%s生约%s岁，情感判定: %s，魅力打分: %s%s" % (
                                            obj['性别'], obj['年龄'], obj['情感'], obj['魅力'], '\n')
                                    else:
                                        content += "这位%s士约%s岁，情感判定: %s，魅力打分: %s%s" % (
                                            obj['性别'], obj['年龄'], obj['情感'], obj['魅力'], '\n')
                            else:
                                image_data = TencentAI_API.Get_Ocr_GeneralOcr_api(image_name)
                                if len(str(image_data)) > 10:
                                    for obj in image_data:
                                        content += "%s%s" % (obj, '\n')
                                    content = content.encode('utf-8')
                                else:
                                    content = '识别失败，要不换个脸大的试试?'
                    except:
                        content = '识别失败，要不换个脸大的试试?'
                    print content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()

                elif recMsg.MsgType == 'voice':
                    if recMsg.Recognition:
                        content_A = recMsg.Recognition
                        retest = talk_api.talks_robot(userid, content_A)
                        if len(retest) > 1993:
                            content_B = retest[:1993] + "......"
                        else:
                            content_B = retest
                    else:
                        content_B = "未开启语音识别功能或者识别内容为空"
                    print 'A:', content_A
                    print 'B:', content_B
                    replyMsg = reply.TextMsg(toUser, fromUser, content_B)
                    return replyMsg.send()

                elif recMsg.MsgType == 'location':

                    location_x = recMsg.Location_X
                    location_y = recMsg.Location_Y
                    content = "您所在的位置：经度" + location_x + "；纬度：" + location_y
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()

                else:
                    return reply.Msg().send()

            elif isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.EventKey == 'mpGuide':
                        content = "设备已绑定"
                        print content
                    if recMsg.EventKey == 'mpGuide_ON':
                        content = "设备已打开"
                        print content
                    if recMsg.EventKey == 'mpGuide_OFF':
                        content = "设备已关闭"
                        print content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()

                elif recMsg.Event == 'pic_photo_or_album':
                    if recMsg.EventKey == 'face_cosmetic':
                        content = "人脸美妆"
                        pic_file = open(text_name, "w+")
                        pic_file.write('fcos')
                        pic_file.close()
                        print content
                    if recMsg.EventKey == 'face_decoration':
                        content = "人脸变妆"
                        pic_file = open(text_name, "w+")
                        pic_file.write('fdec')
                        pic_file.close()
                        print content
                    if recMsg.EventKey == 'face_merge':
                        content = "人脸融合"
                        pic_file = open(text_name, "w+")
                        pic_file.write('fmer')
                        pic_file.close()
                        print content
                    if recMsg.EventKey == 'face_sticker':
                        content = "人脸大头贴"
                        pic_file = open(text_name, "w+")
                        pic_file.write('fsti')
                        pic_file.close()
                        print content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()

            else:
                print "other 暂且不处理\n\n"
                return reply.Msg().send()

        except Exception, Argment:
            return Argment
