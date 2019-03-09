# -*- coding: utf-8 -*-
from random import choice
import urllib.request
import urllib.parse
import ssl


class ZhenziSmsClient(object):
	def __init__(self, apiUrl, appId, appSecret):
		self.apiUrl = apiUrl
		self.appId = appId
		self.appSecret = appSecret

	def random_number(self):
		random_str = []
		seeds = "1234567890"

		for i in range(4):
			random_str.append(choice(seeds))
		return "".join(random_str)
	
	def send(self, number, message, messageId='',): 
		
		data = {
			'appId': self.appId,
			'appSecret': self.appSecret,
			'number': number,
			'messageId': messageId,
			'message': message
		}

		   
		data = urllib.parse.urlencode(data).encode('utf-8')
		ssl._create_default_https_context = ssl._create_unverified_context
		req = urllib.request.Request(self.apiUrl+'/sms/send.do', data=data)
		res_data = urllib.request.urlopen(req)
		res = res_data.read()
		res = res.decode('utf-8')
		return res

	
if __name__ == '__main__':	
	zhen_zi = ZhenziSmsClient("https://sms_developer.zhenzikj.com/","请输入榛子云id 记住是int类型删除双引号","请输入榛子云的appSecret")
	obtain_number = zhen_zi.random_number()
	send_out = zhen_zi.send(message="您的验证码是: {}。如非本人操作，请忽略本短信".format(obtain_number),number='请输入您的手机号')
	print(send_out)