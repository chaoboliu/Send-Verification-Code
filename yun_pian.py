# coding: utf-8
from random import choice
import requests
import json


class YuanPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def random_number(self):
        random_str = []
        seeds = "1234567890"

        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": code
        }
        response = requests.post(self.single_send_url, data=params)
        ret = json.loads(response.text)
        return ret


if __name__ == '__main__':
    yun_pian = YuanPian("请输入云片网的api_key")
    obtain_number = yun_pian.random_number()
    send_out = yun_pian.send_sms('【程序优】欢迎登陆,您的验证码是: {}。如非本人操作，请忽略本短信'.format(obtain_number), '输入您的手机号')
    print(send_out)
