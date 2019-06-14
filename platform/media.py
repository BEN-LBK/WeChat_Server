# -*- coding: utf-8 -*-
# filename: media.py
from basic import Basic
import json
import urllib2
import poster.encode
from poster.streaminghttp import register_openers


class Media(object):
    def __init__(self):
        register_openers()

    # 上传图片
    def uplaod(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print "Uplaod Media Successful"
        return json.loads(urlResp.read())

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()  # 素材的二进制
            image_file_name = "./image/%s.jpg" % mediaId
            mediaFile = file(image_file_name, "wb")
            # mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "Get Media Successful"
            return image_file_name


if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()

    # 新建临时素材
    filePath = "../image/image.jpg"  # 请安实际填写
    mediaType = "image"
    data_dict = myMedia.uplaod(accessToken, filePath, mediaType)
    print data_dict['media_id']
    # 获取临时素材
    #mediaId = "6559152202368476495"
    #myMedia.get(accessToken, mediaId)
