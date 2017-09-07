#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from test_lsh_h5.base.H5Base import H5Base
from test_lsh_mis.base.MisBasic import MisBasic


class H5Basic:
    def __init__(self,enverionment,path):
        self.enverionment = enverionment
        self.path = path

    def getCookie(self):
        base = H5Base(self.enverionment,"",self.path)
        username = base.getUsername()
        password = base.getPassword()
        session = requests.Session()
    
        host = base.getHost()
        headers = eval(base.getHeaders())
        params = {'username': username, 'password': password}
        result = session.post(host + '/account/user/ajaxlogin', params = params)
        if result.json()['ret'] == 1004 :
            #请求验证码
            requests.post(host + '/captcha/sms/sendVerifyUnusual?cellphone=' + username)
            misPath = self.path.replace('h5','mis')
            #misHost = 'http://qa.market-mis.wmdev2.lsh123.com'
            misBasic = MisBasic(self.enverionment,misPath)
            verifyCode = misBasic.getVerifyCode(username)
            user = {'username': username, 'password': password, 'verify_code': verifyCode}
            result = session.post(host + '/account/user/ajaxlogin', params = user, headers=headers)
            
        
        return session
    
    
