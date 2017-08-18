# -*- coding: utf-8 -*-
import os,sys
import logging
import xlrd


class TestCase:
    def getAppTestCase(self,testCasePath,testCaseFile):
        #testCaseFile = os.path.join(os.path.dirname(os.getcwd()) + "/appTestCase",testCaseFile)
        testCaseFile = os.path.join(testCasePath, testCaseFile)
        #print testCaseFile
        if not os.path.exists(testCaseFile):
            logging.error("测试用例文件不存在!")
            sys.exit()
        excel = xlrd.open_workbook(testCaseFile)
        return excel

