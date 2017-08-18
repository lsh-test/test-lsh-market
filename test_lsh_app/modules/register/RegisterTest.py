#-*- coding: utf-8 -*-
import json
import random
import time
import os

from xlutils.copy import copy
from test_lsh_app.base.DB import DB
from test_lsh_app.base.TestCase import TestCase
from test_lsh_app.base.RequestRule import RequestRule
from test_lsh_mis.base.MisBasic import MisBasic

requestRule = RequestRule()
class RegisterTest():
    def __init__(self,host,appConfPath,testCasePath,testCaseDoc,testResultsPath):
        self.host = host
        self.appConfPath = appConfPath
        self.testCaseDoc = testCaseDoc
        self.testCasePath = testCasePath
        self.testResultsPath = testResultsPath

    def registerTest(self):
        print "---------------注册接口测试开始---------------"
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
                #对正常注册的case做特殊处理
                if sheet.cell(i,1).value.encode("utf8") == '正常注册':
                    count = random.randint(0000001,9999999)
                    cellphone = "1600"+str(count)#生成随机手机号
                    params['cellphone'] = int(cellphone)
                    requestRule.get(self.host,"/captcha/sms/regSend","cellphone=" + cellphone)
                    time.sleep(0.5)
                    misConfPath = self.appConfPath.replace('app','mis')
                    misBasic = MisBasic("qa",misConfPath)
                    verifyCode = misBasic.getVerifyCode(cellphone)
                    params['verify_code'] = verifyCode
                ws.write(i, 4, json.dumps(params))
                results = requestRule.post(self.host, url, params)
            # get请求
            elif sheet.cell(i, 2).value == 'get':
                params = sheet.cell(i, 4).value
                if sheet.cell(i,1).value.encode("utf8") == '带邀请码注册':
                    db = DB()
                    data = db.marketQuery("select invite_code from invite_code where uid = 0 and zone_id = 1000 limit 1")
                    for row in data :
                        inviteCode  = row['invite_code']
                    params = params + "&invite_code=" + inviteCode
                #对邀请码与地域不匹配的case特殊处理
                elif sheet.cell(i,1).value.encode("utf8") == '邀请码与地域不匹配':
                    db = DB()
                    data = db.marketQuery("select invite_code from invite_code where uid = 0 and zone_id = 1001 limit 1")
                    for row in data:
                        inviteCode = row['invite_code']
                    params = params+"&invite_code="+inviteCode
                ws.write(i, 4, params)
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
        #wb.save(os.path.dirname(os.getcwd()) + '/appTestResults/registerTestResult_' + resultTime + '.xls')
        wb.save(self.testResultsPath + 'registerTestResult_' + resultTime + '.xls')
        print "---------------注册接口测试结束---------------"
