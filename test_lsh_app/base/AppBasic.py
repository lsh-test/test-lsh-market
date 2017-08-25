#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from test_lsh_app.base.AppBase import AppBase
from test_lsh_mis.base.MisBasic import MisBasic


class AppBasic:
    def __init__(self,host,path):
        self.host = host
        self.path = path

    def getToken(self):
        base = AppBase("","",self.path)
        username = base.getUsername()
        password = base.getPassword()
        host = base.getHost()
        headers = eval(base.getHeaders())
        params = {'username': username, 'password': password}
        result = requests.post(host + '/user/info/login', params = params)
        if result.json()['ret'] == 1004 :
            #请求验证码
            requests.post(host + '/captcha/sms/sendVerifyUnusual?cellphone=' + username)
            misPath = self.path.replace('app','mis')
            misHost = 'qa.market-mis.wmdev2.lsh123.com'
            misBasic = MisBasic(misHost,misPath)
            verifyCode = misBasic.getVerifyCode(username)
            user = {'username': username, 'password': password, 'verify_code': verifyCode}
            result = requests.post(host + '/user/info/login', params = user, headers=headers)
        token = result.json()['content']['token']
        return token
