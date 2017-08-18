#-*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.base.AppRunSystemEnv import AppRunSystemEnv
from test_lsh_app.modules.login.LoginTest import LoginTest
from test_lsh_app.modules.register.RegisterTest import RegisterTest

from test_lsh_app.modules.homepage.HomePageTest import HomePageTest

base_dir=str(os.path.dirname(__file__))

print base_dir

class TestApp(unittest.TestCase):
    def setUp(self):
        self.enveriment = sys.argv[1]  # app环境
        appSysPath = AppRunSystemEnv()
        self.appConfpath = appSysPath.getPath(sys.argv[2])[0] #appConf路径
        self.testCasePath = appSysPath.getPath(sys.argv[2])[1] #appTestCase路径
        self.testResultsPath = appSysPath.getPath(sys.argv[2])[2] #appTestResults路径
        appBase = AppBase(self.enveriment,self.appConfpath,"")
        self.host = appBase.getHost()

    def tearDown(self):
        pass

    #测试登录
    def testLogin(self):
        appBase = AppBase(self.enveriment,self.appConfpath,"login")
        testCaseDoc = appBase.getTestCaseDoc()#获得登录testcase文件
        loginTest = LoginTest(self.host,self.testCasePath,testCaseDoc,self.testResultsPath)#登录测试
        loginTest.loginTest()

    #测试注册
    def testRegister(self):
        appBase = AppBase(self.enveriment,self.appConfpath,"register")
        testCaseDoc = appBase.getTestCaseDoc()#获得注册testcase文件
        registerTest = RegisterTest(self.host,self.appConfpath,self.testCasePath,testCaseDoc,self.testResultsPath)#注册测试
        registerTest.registerTest()
        
    #测试app首页
    def testHomePage(self):
        appBase=AppBase(self.enveriment,self.appConfpath,"homepage")
        
        testCaseDoc = appBase.getTestCaseDoc()#获得首页testcase文件
        homepageTest=HomePageTest(self.host,self.appConfpath,self.testCasePath,testCaseDoc,self.testResultsPath)
        homepageTest.HomePageTest()
        
    
    
    
    def createsuite(self):
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(base_dir,pattern='.*Test.py', top_level_dir=None)
        for test_suite in discover:
            for testsuit in test_suite:
                testunit.addTest(testsuit)
        return testunit
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestApp("testLogin"))
    suite.addTest(TestApp("testRegister"))
    suite.addTest(TestApp("testHomePage"))
    
    

    runner = unittest.TextTestRunner()
    runner.run(suite)