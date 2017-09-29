#-*- coding: utf-8 -*-
import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from test_lsh_app.base.SendMail import SendMail
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.base.AppRunSystemEnv import AppRunSystemEnv
from test_lsh_app.modules.login.LoginTest import LoginTest
from test_lsh_app.modules.register.RegisterTest import RegisterTest
from test_lsh_app.modules.mypage.MyPageTest import MyPageTest
from test_lsh_app.modules.homepage.HomePageTest import HomePageTest
from test_lsh_app.modules.shopping_cart_page.ShoppingCartPageTest import ShoppingCartPageTest
from test_lsh_app.modules.classifypage.ClassifyPageTest import ClassifyPageTest

#base_dir=str(os.path.dirname(os.path.dirname(__file__)))

testResultFilelist = []
class TestApp(unittest.TestCase):
    def setUp(self):

        self.enverionment = sys.argv[1]  # app环境
        appSysPath = AppRunSystemEnv()
        self.appConfpath = appSysPath.getPath(sys.argv[2])[0] #appConf路径
        self.testCasePath = appSysPath.getPath(sys.argv[2])[1] #appTestCase路径
        self.testResultsPath = appSysPath.getPath(sys.argv[2])[2] #appTestResults路径
        appBase = AppBase(self.enverionment,self.appConfpath,"")
        self.host = appBase.getHost()

    def tearDown(self):
        pass

    def getargvs(self,name):
        appBase = AppBase(self.enverionment,self.appConfpath,name)
        testCaseDoc = appBase.getTestCaseDoc()
        args = (self.enverionment,self.host,self.appConfpath,self.testCasePath,testCaseDoc,self.testResultsPath)
        return args

    #测试登录
    def testLogin(self):
        loginTest = LoginTest(*self.getargvs("login"))
        loginResultFile = loginTest.loginTest()
        testResultFilelist.append(loginResultFile)

    #测试注册
    def testRegister(self):
        registerTest = RegisterTest(*self.getargvs("register"))#注册测试
        registerResultFile = registerTest.registerTest()
        testResultFilelist.append(registerResultFile)

    #测试app首页
    def testHomePage(self):
        homepageTest=HomePageTest(*self.getargvs("homepage"))
        homepageResultFile = homepageTest.HomePageTest()
        testResultFilelist.append(homepageResultFile)
        
    #测试我的页面
    def testMyPage(self):
        mypageTest=MyPageTest(*self.getargvs("mypage"))
        myResultFile = mypageTest.MyPageTest()
        testResultFilelist.append(myResultFile)

    #测试购物车页面接口
    def testShoppingCartPage(self):
        shoppingCartpageTest=ShoppingCartPageTest(*self.getargvs("shopping_cart_page"))
        shoppingCartpageResultFile = shoppingCartpageTest.ShoppingCartPageTest()
        testResultFilelist.append(shoppingCartpageResultFile)

    #测试分类页接口
    def testClassifyPage(self):
        classifyPageTest=ClassifyPageTest(*self.getargvs("classifypage"))
        classifyPageResultFile = classifyPageTest.ClassifyPageTest()
        testResultFilelist.append(classifyPageResultFile)
    
    """ def createsuite(self):
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(base_dir,pattern='test*.py', top_level_dir=None)
        for test_suite in discover:
            for testsuit in test_suite:
                testunit.addTest(testsuit)
        return testunit"""

    #以邮件形式发送测试结果
    def testSendResultFile(self):
        sendMail = SendMail()
        sendMail.mail(testResultFilelist)
        #print testResultFilelist

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestApp("testLogin"))
    suite.addTest(TestApp("testRegister"))
    suite.addTest(TestApp("testHomePage"))
    suite.addTest(TestApp("testMyPage"))
    suite.addTest(TestApp("testShoppingCartPage"))
    suite.addTest(TestApp("testClassifyPage"))

    suite.addTest(TestApp("testSendResultFile"))#发邮件

    runner = unittest.TextTestRunner()
    runner.run(suite)