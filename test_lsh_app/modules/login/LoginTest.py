#-*- coding: utf-8 -*-
import time
import os

from xlutils.copy import copy
from test_lsh_app.base.TestCase import TestCase
from test_lsh_app.base.RequestRule import RequestRule

requestRule = RequestRule()
class LoginTest():
    def __init__(self,host,testCasePath,testCaseDoc,testResultsPath):
        self.host = host
        self.testCasePath = testCasePath
        self.testCaseDoc = testCaseDoc
        self.testResultsPath = testResultsPath
        print self.testResultsPath

    def loginTest(self):
        print "---------------登录接口测试开始---------------"
        testCase = TestCase()
        excel = testCase.getAppTestCase(self.testCasePath,self.testCaseDoc)
        sheet = excel.sheets()[0]
        nrows = sheet.nrows
        wb = copy(excel)
        ws = wb.get_sheet(0)
        amount = 0
        for i in range(1, nrows):
            url = sheet.cell(i, 3).value
            # post请求
            if sheet.cell(i, 2).value == 'post':
                params = eval(sheet.cell(i, 4).value)
                results = requestRule.post(self.host, url, params)
            # get请求
            elif sheet.cell(i, 2).value == 'get':
                params = sheet.cell(i, 4).value
                results = requestRule.get(self.host, url, params)
            resultTime = results[0]
            resultStatus = results[1]
            resultText = results[2]
            ws.write(i, 7, resultTime)
            status = sheet.cell(i, 5).value
            if resultStatus == status:
                print "第%d条用例pass" % i
                ws.write(i, 6, "pass")
                amount += 1
            else:
                print "第%d条用例failure" % i
                ws.write(i, 6, resultText)
        a = (amount / float(i))*100
        ws.write(i, 9, "%.2f" % a + "%")
        print "case通过率为%.2f" % a + "%"
        resultTime = time.strftime('%Y-%m-%d_%H:%M:%S')
        #wb.save(os.path.dirname(os.getcwd()) + '/appTestResults/loginTestResult' + resultTime + '.xls')
        wb.save(self.testResultsPath + 'loginTestResult_' + resultTime + '.xls')
        print "---------------登录接口测试结束---------------"
