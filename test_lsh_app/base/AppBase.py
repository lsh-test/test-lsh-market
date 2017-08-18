#-*- coding: utf-8 -*-
import ConfigParser
import os

cf = ConfigParser.ConfigParser()
#cf.read(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]) + "/conf/app_config.ini")

class AppBase:
    def __init__(self,environment,confPath,module):
        self.environment = environment
        self.module = module
        cf.read(confPath)

    def getUsername(self):
        username = cf.get("app_user","username")
        return username

    def getPassword(self):
        password = cf.get("app_user","password")
        return password

    def getHeaders(self):
        headers = cf.get("app_headers","headers")
        return headers

    def getHost(self):
        if self.environment == 'qa':
            host = cf.get("app_host","qa_host")
            return host
        elif self.environment == 'qa2':
            host = cf.get("app_host", "qa2_host")
            return host
        elif self.environment == 'qa3':
            host = cf.get("app_host", "qa3_host")
            return host
        else :
            print "环境不存在!"

    def getTestCaseDoc(self):
        if self.module == 'login':
            testCaseDoc = cf.get("test_case_doc","loginCase")
            return testCaseDoc
        elif self.module == 'register':
            testCaseDoc = cf.get("test_case_doc", "registerCase")
            return testCaseDoc
        else :
            print "testcase不存在!"

