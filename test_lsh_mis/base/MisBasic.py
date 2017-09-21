import requests

from test_lsh_mis.base.MisBase import MisBase


class MisBasic():
    def __init__(self,enverionment,path):
        self.enverionment = enverionment
        self.path = path

    def getCookie(self):
        misBase = MisBase(self.enverionment,"",self.path)
        host = misBase.getHost()
        email = misBase.getEmail()
        password = misBase.getPassword()
        params = {'email': email, 'pwd': password}
        result = requests.post(host + '/account/user/checklogin', params = params)
        cookies = result.headers.get('Set-Cookie')
        return cookies

    def getVerifyCode(self,username):
        misBase = MisBase(self.enverionment, "", self.path)
        host = misBase.getHost()
        headers = {'Cookie': self.getCookie()}
        result = requests.get(host + '/customermanage/user/searchverify?cellphone=' + username, headers=headers)
        
        resultContent = result.json()['content'][0]
        verifyCode = resultContent['verify_code']
        return verifyCode
