#-*- coding: utf-8 -*-
class H5RunSystemEnv:
    #系统路径
    def getPath(self,systemEnv):
        pathList = []
        if systemEnv == 'zhouxin':
            confPath = "/Users/zhouxin/PycharmProjects/test-lsh-market/test_lsh_app/conf/app_config.ini"
            testCasePath = "/Users/zhouxin/PycharmProjects/test-lsh-market/test_lsh_app/appTestCase/"
            testResultPath = "/Users/zhouxin/PycharmProjects/test-lsh-market/test_lsh_app/appTestResults/"
            pathList.append(confPath)
            pathList.append(testCasePath)
            pathList.append(testResultPath)
            return pathList

        elif systemEnv== 'CI':
            confPath = "/home/work/test-env/jenkins/workspace/test-lsh-market/test_lsh_app/conf/app_config.ini"
            testCasePath = "/home/work/test-env/jenkins/workspace/test-lsh-market/test_lsh_app/appTestCase/"
            testResultPath = "/home/work/test-env/jenkins/workspace/test-lsh-market/test_lsh_app/appTestResults/"
            pathList.append(confPath)
            pathList.append(testCasePath)
            pathList.append(testResultPath)
            return pathList
        elif systemEnv=="zyb":
            confPath = "D://test-lsh-market//test_lsh_h5//conf//h5_config.ini"
            testCasePath = "D://test-lsh-market//test_lsh_h5//h5TestCase/"
            testResultPath = "D://test-lsh-market//test_lsh_h5//h5TestResults/"
            pathList.append(confPath)
            pathList.append(testCasePath)
            pathList.append(testResultPath)
            return pathList
            

