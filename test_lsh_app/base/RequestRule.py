#-*- coding: utf-8 -*-
import requests


class RequestRule:

    #get请求方法
    def get(self,host,url,params):
        resultlist = []
        try:
            result = requests.get(host + url + "?" + params)
            responseTime = (result.elapsed.microseconds) / 1000
            ret = result.json()['ret']
            resultlist.append(responseTime)
            resultlist.append(ret)
            resultlist.append(result.text)
        except Exception,e:
            print Exception,":",e
        return resultlist

    #post请求方法
    def post(self,host,url,params):
        resultlist = []
        try:
            result = requests.post(host + url, params=params)
            responseTime = (result.elapsed.microseconds) / 1000
            ret = result.json()['ret']
            resultlist.append(responseTime)
            resultlist.append(ret)
            resultlist.append(result.text)
        except Exception,e:
            print Exception,":",e
        return resultlist