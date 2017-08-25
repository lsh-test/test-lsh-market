import requests

from test_lsh_mis.base.MisBase import MisBase


class MisBasic():
    def __init__(self,host,path):
        self.host = host
        self.path = path

    def getCookie(self):
        misBase = MisBase("","",self.path)
        email = misBase.getEmail()
        password = misBase.getPassword()
        params = {'email': email, 'pwd': password}
        result = requests.post(self.host + '/account/user/checklogin', params = params)
        cookies = result.headers.get('Set-Cookie')
        return cookies

    def getVerifyCode(self,username):
        misBase = MisBase("", "", self.path)
        misHost = misBase.getHost()
        headers = {'Cookie': self.getCookie()}
        result = requests.get(misHost + '/customermanage/user/searchverify?cellphone=' + username, headers=headers)
        resultContent = result.json()['content'][0]
        verifyCode = resultContent['verify_code']
        return verifyCode
