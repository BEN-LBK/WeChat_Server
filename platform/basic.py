# -*- coding: utf-8 -*-
# filename: basic.py

import urllib
import time
import json

class Basic:    
	def __init__(self):        
		self.__accessToken = ''        
		self.__leftTime = 0    

	def __real_get_access_token(self):        
		appId = "wx8ec8e93bf38d9943"        
		appSecret = "76e6f1f4cfc6e2e37e65cc4736d7b3fe"     
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))        
		urlResp = urllib.urlopen(postUrl)        
		urlResp = json.loads(urlResp.read())                
		self.__accessToken = urlResp['access_token']    
		#print "\nthe new get accessToken: %s\n", self.__accessToken    
		self.__leftTime = urlResp['expires_in']   

	def get_access_token(self):        
		if self.__leftTime < 10:            
			self.__real_get_access_token()        
			return self.__accessToken



	def run(self):        
		while(True):            
			if self.__leftTime > 10:                
				time.sleep(2)                
				self.__leftTime -= 2            
			else:                
				self.__real_get_access_token()