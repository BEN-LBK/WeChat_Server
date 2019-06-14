# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Basic


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [          
            {
                "name": "稍微看看",
                "sub_button":
                [
                    {
                        "type": "media_id",
                        "name": "Jay Chou",
                        "media_id": "lPg7Bjq3ZoJ5Y570QXDIgbd11B0kQQaQCwEyUciNMFU"
                    },
                    {
                        "type": "view",
                        "name": "等你下课",
                        "url": "https://data.vod.itc.cn/?new=/88/151/88zTiK8NKN7QqDn8cvSLue.mp4&vid=4472079&plat=17&mkey=cbX-PS1pV_3LJynr1tx8YzYSZ5czbLui&ch=tv&user=api&uid=1804092241387640&SOHUSVP=wx3E9qzFm5gObInPoWZxlj-_J9oH1-ekkSX-SZK6mO4&pt=5&prod=h5&pg=1&eye=0&cv=1.0.0&qd=68000&src=11100001&ca=4&cateCode=121&_c=1&appid=tv&oth=&cd="
                    },


                    {
                        "type": "view",
                        "name": "杰伦百科",
                        "url": "https://baike.baidu.com/item/周杰伦/129156?fr=aladdin"
                    }

                ]
            },
        
            {
                "name": "人脸特效",
                "sub_button": 
                [
                    {
                        "type": "pic_photo_or_album", 
                        "name": "人脸美妆", 
                        "key": "face_cosmetic", 
                        "sub_button": [ ]    
                     }, 
                    {
                        "type": "pic_photo_or_album", 
                        "name": "人脸变妆", 
                        "key": "face_decoration", 
                        "sub_button": [ ]
                    }, 
                    {
                        "type": "pic_photo_or_album", 
                        "name": "人脸融合", 
                        "key": "face_merge", 
                        "sub_button": [ ]
                    },
                    {
                        "type": "pic_photo_or_album", 
                        "name": "人脸大头贴", 
                        "key": "face_sticker", 
                        "sub_button": [ ]
                    }
                ]
            },
            {
                "name": "设备测试",
                "sub_button":
                [
                    {
                        "type": "click",
                        "name": "设备绑定",
                        "key":  "mpGuide"
                    },
                    {
                        "type": "click",
                        "name": "设备打开",
                        "key":  "mpGuide_ON"
                    },
                    {
                        "type": "click",
                        "name": "设备关闭",
                        "key":  "mpGuide_OFF"
                    }
                ]
            }
        ]
    }
    """
    accessToken = Basic().get_access_token()
    myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
