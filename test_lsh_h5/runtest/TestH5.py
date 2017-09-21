#-*- coding: utf-8 -*-
import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
 
from test_lsh_h5.base.H5Base import H5Base  
from test_lsh_h5.base.H5RunSystemEnv import H5RunSystemEnv
from test_lsh_h5.modules.login.LoginTest import LoginTest
from test_lsh_h5.modules.register.RegisterTest import RegisterTest
from test_lsh_h5.modules.mypage.MyPageTest import MyPageTest
from test_lsh_h5.modules.homepage.HomePageTest import HomePageTest
from test_lsh_h5.modules.shopping_cart_page.ShoppingCartPageTest import ShoppingCartPageTest
from test_lsh_h5.modules.classifypage.ClassifyPageTest import ClassifyPageTest

#base_dir=str(os.path.dirname(os.path.dirname(__file__)))


class TestH5(unittest.TestCase):
    def setUp(self):
        self.enverionment = sys.argv[1]  # app环境
        h5SysPath = H5RunSystemEnv()
        self.h5Confpath = h5SysPath.getPath(sys.argv[2])[0] #appConf路径
        self.testCasePath = h5SysPath.getPath(sys.argv[2])[1] #appTestCase路径
        self.testResultsPath = h5SysPath.getPath(sys.argv[2])[2] #appTestResults路径
        h5Base = H5Base(self.enverionment,self.h5Confpath,"")
        self.host = h5Base.getHost()

    def tearDown(self):
        pass
    
    
    def getargvs(self,name):
        h5Base = H5Base(self.enverionment,self.h5Confpath,name)
        testCaseDoc = h5Base.getTestCaseDoc()
        args=(self.enverionment,self.host,self.h5Confpath,self.testCasePath,testCaseDoc,self.testResultsPath)
        return args
    #测试登录
    def testLogin(self):
        #h5Base = H5Base(self.enverionment,self.h5Confpath,"login")
        #testCaseDoc = h5Base.getTestCaseDoc()#获得登录testcase文件
        loginTest = LoginTest(*self.getargvs("login"))#登录测试
        loginTest.loginTest()

    #测试注册
    def testRegister(self):
        #h5Base = H5Base(self.enverionment,self.h5Confpath,"register")
        #testCaseDoc = h5Base.getTestCaseDoc()#获得注册testcase文件
        registerTest = RegisterTest(*self.getargvs("register"))#注册测试
        registerTest.registerTest()
        
    #测试app首页
    def testHomePage(self):
        #h5Base=H5Base(self.enverionment,self.h5Confpath,"homepage")
        #testCaseDoc = h5Base.getTestCaseDoc()#获得首页testcase文件
        homepageTest=HomePageTest(*self.getargvs("homepage"))
        homepageTest.HomePageTest()
        
    #测试我的页面
    def testMyPage(self):
        #h5Base=H5Base(self.enverionment,self.h5Confpath,"mypage")
        
        #testCaseDoc = h5Base.getTestCaseDoc()#获得我的页面testcase文件
        mypageTest=MyPageTest(*self.getargvs("mypage"))
        mypageTest.MyPageTest()
    #测试购物车页面接口
    def testShoppingCartPage(self):
        
        #h5Base=H5Base(self.enverionment,self.h5Confpath,"shopping_cart_page")
        
        #testCaseDoc = h5Base.getTestCaseDoc()#获得购物车页面testcase文件
        shoppingCartpageTest=ShoppingCartPageTest(*self.getargvs("shopping_cart_page"))
        shoppingCartpageTest.ShoppingCartPageTest()
    #测试分类页接口
    def testClassifyPage(self):
        
        #h5Base=H5Base(self.enverionment,self.appConfpath,"classifypage")
        
        #testCaseDoc = h5Base.getTestCaseDoc()#获得分类页面testcase文件
        classifyPageTest=ClassifyPageTest(*self.getargvs("classifypage"))
        classifyPageTest.ClassifyPageTest()
    
    """ def createsuite(self):
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(base_dir,pattern='test*.py', top_level_dir=None)
        for test_suite in discover:
            for testsuit in test_suite:
                testunit.addTest(testsuit)
        return testunit"""
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestH5("testLogin"))
    suite.addTest(TestH5("testHomePage"))
    #suite.addTest(TestH5("testRegister"))
    
    '''suite.addTest(TestApp("testRegister"))
    suite.addTest(TestApp("testHomePage"))
    suite.addTest(TestApp("testMyPage"))
    suite.addTest(TestApp("testShoppingCartPage"))
    suite.addTest(TestApp("testClassifyPage"))'''

    runner = unittest.TextTestRunner()
    runner.run(suite)